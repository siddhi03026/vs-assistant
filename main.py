from fastapi import FastAPI, UploadFile, File, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from loguru import logger
import os
from utils.video_processor import process_video
from utils.summarizer import summarize_events
from utils.chat_handler import ChatHandler

app = FastAPI()
logger.add("logs.log", rotation="500 KB")

# Serve frontend
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

# Memory for multi-turn chat
chat_handler = ChatHandler()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/upload/")
async def upload_video(file: UploadFile = File(...)):
    try:
        file_location = f"{UPLOAD_DIR}/{file.filename}"
        with open(file_location, "wb") as buffer:
            buffer.write(await file.read())
        logger.info(f"Video uploaded: {file.filename}")

        # Event recognition from video
        events = process_video(file_location)

        # Summarize events
        summary = summarize_events(events)

        # Save to chat memory
        chat_handler.store_summary(summary)

        return JSONResponse({
            "filename": file.filename,
            "events": events,
            "summary": summary
        })

    except Exception as e:
        logger.exception("Error during video upload")
        return JSONResponse(status_code=500, content={"error": str(e)})


@app.post("/chat/")
async def chat_endpoint(payload: dict):
    try:
        user_input = payload.get("message", "")
        response = chat_handler.respond(user_input)
        return {"response": response}
    except Exception as e:
        logger.exception("Error in chat")
        return JSONResponse(status_code=500, content={"error": str(e)})
