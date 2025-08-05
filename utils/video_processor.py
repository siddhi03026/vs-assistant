import cv2
import os
import numpy as np
from datetime import timedelta
from loguru import logger

def format_timestamp(seconds):
    return str(timedelta(seconds=int(seconds)))

def process_video(video_path: str):
    logger.info(f"Processing video: {video_path}")
    events = []

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        logger.error("Failed to open video.")
        return []

    fps = int(cap.get(cv2.CAP_PROP_FPS))
    frame_count = 0
    event_interval = 30  # Check for event every 30 frames

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame_count += 1

        # Dummy event trigger every 150 frames
        if frame_count % 150 == 0:
            seconds = int(frame_count / fps)
            timestamp = format_timestamp(seconds)

            # Simulated events
            sample_event = {
                "event": "Simulated Vehicle Detected",
                "type": "Car",
                "timestamp": timestamp
            }
            events.append(sample_event)
            logger.debug(f"Detected event at {timestamp}")

    cap.release()
    logger.success(f"Extracted {len(events)} events.")
    return events
