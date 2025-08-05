from loguru import logger

def summarize_events(events: list) -> str:
    logger.info("Generating summary from events")

    if not events:
        return "No significant events were detected in the video."

    summary_lines = []

    for event in events:
        event_type = event.get("event", "Unknown Event")
        obj_type = event.get("type", "object")
        timestamp = event.get("timestamp", "unknown time")

        summary_lines.append(
            f"{event_type} involving a {obj_type} was observed at {timestamp}."
        )

    summary = " ".join(summary_lines)
    logger.success("Summary generated successfully")
    return summary
