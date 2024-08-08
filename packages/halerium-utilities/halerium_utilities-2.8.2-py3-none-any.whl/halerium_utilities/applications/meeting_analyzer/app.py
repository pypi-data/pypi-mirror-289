# fastapi imports
from fastapi import FastAPI, UploadFile, File, Form, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
import uvicorn

# infrastructure imports
import argparse
import base64
from datetime import datetime
import json
import logging
import numpy as np
import os
from pathlib import Path
from uuid import uuid4

# backend imports
from .src.args import CLIArgs
from .src.transcribe_audiofile import transcribe_audio
from .src.audio_processor import AudioProcessor
from .src.template_analyzer import analyze_snippet
from .src.infostore_handler import (
    push_summaries_to_infostore,
    push_transcript_to_infostore,
    fetch_infostore,
)
from .src.board_utils import create_meeting_board, get_meeting_board_deep_link

# halerium utilities imports
from halerium_utilities.collab import CollabBoard


def parse_args(args=None):
    # get start up parameters
    arg_parser = argparse.ArgumentParser(description="Polybot API")

    for arg in CLIArgs.args.values():
        names_or_flags = arg.pop("name_or_flags", [])
        arg_parser.add_argument(*names_or_flags, **arg)

    # parse cli and board arguments
    cli_args = arg_parser.parse_args(args)
    return cli_args


cli_args = parse_args()

# setup logging with debug level
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)

# Global variable to store transcripts
# TODO: needs to be changed at some point to a database or similar
transcripts = {}

# Global variable to store active sessions
# TODO: needs to be changed at some point to a database or similar
sessions = {}

meeting_template = Path(cli_args.board)

# create directories for storing audio files and meeting boards, define the app's root path
meetings_path = Path(cli_args.meetings_path)
meetings_path.mkdir(exist_ok=True, parents=True)
audio_upload_path = Path(cli_args.upload_path)
audio_upload_path.mkdir(exist_ok=True, parents=True)

# infor stores
summary_info_store_name = cli_args.summary_store
try:
    fetch_infostore(summary_info_store_name)
except Exception as exc:
    logger.debug(f"No store with the name {summary_info_store_name} found.")
    raise exc
transcript_info_store_name = cli_args.transcript_store
try:
    fetch_infostore(transcript_info_store_name)
except:
    raise RuntimeError(f"No store with the name {transcript_info_store_name} found.")

# ports
port_app = cli_args.port
port_chatbot = cli_args.cbport

root_path = (
    f"/apps/{os.getenv('HALERIUM_ID')}/{str(port_app)}/"
    if os.getenv("HALERIUM_ID")
    else ""
)
frontend_path = Path(__file__).resolve().parent / "frontend"

# create the FastAPI app
app = FastAPI(root_path=root_path)


# mount static files and define templates directory
app.mount(
    "/static",
    StaticFiles(directory=frontend_path),
    name="static",
)
templates = Jinja2Templates(directory=frontend_path / "templates")

# chatbot link
chatbot_link = (
    f"{os.getenv('HALERIUM_BASE_URL')}/apps/{os.getenv('HALERIUM_ID')}/{port_chatbot}"
)
app_link = (
    f"{os.getenv('HALERIUM_BASE_URL')}/apps/{os.getenv('HALERIUM_ID')}/{port_app}"
)


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):

    return templates.TemplateResponse(
        "mode-selector.html",
        {
            "request": request,
            "chatbot_link": chatbot_link,
        },
    )


@app.get("/create_session")
async def create_session():
    """
    Create a new session and return the session_id.

    Returns:
        dict: session_id
    """
    global sessions

    new_session_id = str(uuid4())

    sessions[new_session_id] = {
        "session_id": new_session_id,
        "start_time": None,
        "end_time": None,
        "active_ws": None,
    }
    return {"session_id": new_session_id}


@app.get("/meeting", response_class=HTMLResponse)
async def meeting(request: Request):

    return templates.TemplateResponse(
        "meeting.html",
        {
            "request": request,
            "chatbot_link": chatbot_link,
        },
    )


@app.post("/upload", response_class=HTMLResponse)
async def upload(request: Request, fileInputs: list[UploadFile] = File(...)):

    file_names = [file.filename for file in fileInputs]

    for file in fileInputs:

        # if file does not already exist, write it to disk
        file_path = Path(audio_upload_path / file.filename)
        if not file_path.exists():

            with open(file_path, "wb") as f:
                f.write(file.file.read())

    return templates.TemplateResponse(
        "uploaded_files_list.html",
        {
            "request": request,
            "chatbot_link": chatbot_link,
            "file_names": file_names,
        },
    )


@app.websocket("/record_and_transcribe/{session_id}")
async def record_and_transcribe(websocket: WebSocket, session_id: str):
    """
    Websocket connection for the audio stream.
    """
    global sessions, transcripts
    await websocket.accept()
    audio_processor = None

    # check if session_id is valid
    if session_id not in sessions:
        logger.error(f"Invalid session_id: {session_id}")
        await websocket.close()

    # check if session is already active
    if sessions[session_id]["active_ws"]:
        logger.error(f"Session {session_id} is already active.")
        await websocket.close()
    else:
        logger.info(f"Session {session_id} started.")
        start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sessions[session_id]["active_ws"] = websocket
        sessions[session_id]["start_time"] = start_time

    try:
        while True:
            # receive data
            data = await websocket.receive()

            # start/stop recording
            if "text" in data:

                # if "ping" is received, send "pong":
                if data["text"] == "ping":
                    await websocket.send_text("pong")
                    continue

                message = json.loads(data.get("text"))

                if message["type"] == "audio-start":
                    samplerate = message["samplerate"]
                    audio_processor = AudioProcessor(int(samplerate), session_id)
                    sessions[session_id]["audio_processor"] = audio_processor
                    logger.debug(
                        f"{session_id} started recording ({samplerate} Hz -> {samplerate * 16/8} bytes/sec)"
                    )

                elif message["type"] == "audio-end":
                    logger.debug(f"{session_id} stopped recording")
                    sessions[session_id]["audio_processor"].is_recording = False
                    filename = sessions[session_id]["audio_processor"].export_to_mp3()
                    logger.debug(f"{session_id} created file: {filename}")
                    sessions[session_id]["mp3_name"] = filename
                    sessions[session_id]["audio_processor"] = None

            # receive audio data
            elif "bytes" in data:
                if (
                    sessions[session_id]["audio_processor"]
                    and sessions[session_id]["audio_processor"].is_recording
                ):
                    byte_data = data.get("bytes")
                    sessions[session_id]["audio_processor"].write_chunk(byte_data)

    except WebSocketDisconnect:
        logger.debug(f"{session_id}: AudioWebSocket disconnected.")

    except RuntimeError as e:
        logger.error(f"{session_id}: AudioWebsocket RuntimeError: {e}")

    finally:
        # remove from active sessions
        sessions[session_id]["active_ws"] = None


@app.get("/generate_transcript/{session_id}")
async def generate_transcript(request: Request, session_id: str):
    """
    Converts the 16-bit PCM audio data to an mp3 and transcribes it.

    Args:
        session_id (str): The user session_id
    """
    global transcripts, sessions

    # if there is no filename, but still an audio recorder, then the websocket connection apparently failed to sent the audio-end message
    # and we still need convert the raw temp file to an mp3
    if (
        not "mp3_name" in sessions[session_id]
        and sessions[session_id]["audio_processor"]
    ):
        logger.debug(f"{session_id} stopped recording")
        filename = sessions[session_id]["audio_processor"].export_to_mp3()
        (
            logger.debug(f"{session_id} created potentially partial file: {filename}")
            if filename
            else logger.error(f"Failed to export temp file to mp3 for {session_id}")
        )

        sessions[session_id]["mp3_name"] = filename

    # if there is a filename the audio file was already created
    elif "mp3_name" in sessions[session_id] and sessions[session_id]["mp3_name"]:
        logger.debug(f"Found existing mp3 file: {sessions[session_id]['mp3_name']}")

    try:
        audio_b64 = ""
        with open(sessions[session_id]["mp3_name"], "rb") as uploaded_file:
            audio_b64 = base64.b64encode(uploaded_file.read()).decode("utf-8")

        logger.debug(f"Transcribing audio file: {sessions[session_id]['mp3_name']}")
        transcript = transcribe_audio(audio_b64)
        transcripts[session_id] = transcript

    except Exception as e:
        logger.error(f"Error transcribing audio file: {e}")
        transcripts[session_id] = "Error transcribing audio file."
        return {"status": "error", "result": "Error transcribing audio file."}
    else:
        # send ready message to client
        return {"status": "success", "result": "Transcription successful."}


@app.get("/analyze_transcript/{session_id}", response_class=HTMLResponse)
async def analyze_transcript(request: Request, session_id: str):

    # get the transcript from the current session
    global transcripts
    transcript = transcripts[session_id]

    # create a meeting board from the transcript
    meeting_board_path = create_meeting_board(
        transcript, meetings_path=meetings_path, meeting_template=meeting_template
    )

    # get the deep link to the meeting board
    deep_link = get_meeting_board_deep_link(meeting_board_path)

    # returns a dict of card_ids and corresponding prompt outputs
    analysis_output = analyze_snippet(meeting_board_path)

    return templates.TemplateResponse(
        "analysis.html",
        {
            "request": request,
            "chatbot_link": chatbot_link,
            "analysis_output": analysis_output,
            "meeting_board_path": meeting_board_path,
            "deep_link": deep_link,
            "transcript": transcript,
        },
    )


@app.post("/transcribe_and_analyze_files")
async def transcribe_and_analyze_files(
    request: Request, fileNames: list[str] = Form(...)
):
    if not fileNames:
        return {"error": "No file selected"}

    full_transcript = ""
    fileNames = fileNames[0].split(",")

    for filename in fileNames:
        audiofile_path = os.path.join(audio_upload_path, filename)
        audio_b64 = ""
        with open(audiofile_path, "rb") as uploaded_file:
            audio_b64 = base64.b64encode(uploaded_file.read()).decode("utf-8")

        # get the transcript for all files
        transcript = transcribe_audio(audio_b64)
        full_transcript += "\n\n\n" + transcript

    # create a meeting board from the transcript
    meeting_board_path = create_meeting_board(
        full_transcript, meetings_path=meetings_path, meeting_template=meeting_template
    )

    # get the deep link to the meeting board
    deep_link = get_meeting_board_deep_link(meeting_board_path)

    # returns a dict of card_ids and corresponding prompt outputs
    analysis_output = analyze_snippet(meeting_board_path)

    return templates.TemplateResponse(
        "analysis.html",
        {
            "request": request,
            "chatbot_link": chatbot_link,
            "analysis_output": analysis_output,
            "meeting_board_path": meeting_board_path,
            "deep_link": deep_link,
            "transcript": full_transcript,  # update
        },
    )


@app.post("/approve_and_postprocess")
async def approve_and_postprocess(
    request: Request,
):

    r = await request.json()

    meeting_board_path = r.get("board_path")
    approved_analysis = r.get("approved")
    transcript = r.get("transcript")

    if meeting_board_path and approved_analysis:
        board = CollabBoard(meeting_board_path, pull_on_init=True)

        summaries = ""
        for card_id, analysis in approved_analysis.items():
            chunk = analysis
            board.update_card(
                {"id": card_id, "type_specific": {"prompt_output": chunk}}
            )
            board.push()

            summaries += chunk + "\n\n"

        meeting_title, meeting_id = push_summaries_to_infostore(
            [summaries], info_store_name=summary_info_store_name
        )  # push the summaries to infostore
        push_transcript_to_infostore(
            transcript,
            info_store_name=transcript_info_store_name,
            meeting_title=meeting_title,
            meeting_id=meeting_id,
        )

        return {
            "status": "success",
            "message": "Analysis successfully approved and pushed to infostore.",
        }

    return {"status": "error", "message": "No board path or approved analysis found."}


@app.get("/success")
async def success(request: Request, deep_link: str, success: bool):

    if success:

        return templates.TemplateResponse(
            "success.html",
            {
                "request": request,
                "chatbot_link": chatbot_link,
                "deep_link": deep_link,
            },
        )

    else:

        return templates.TemplateResponse(
            "error.html",
            {
                "request": request,
                "chatbot_link": chatbot_link,
                "deep_link": deep_link if not deep_link == "None" else None,
            },
        )


def main():

    uvicorn.run(app, host="0.0.0.0", port=port_app)
