from loguru import logger

class ChatHandler:
    def __init__(self):
        self.memory = {
            "summary": "",
            "chat_history": []
        }

    def store_summary(self, summary: str):
        self.memory["summary"] = summary
        self.memory["chat_history"] = []  # Reset on new video
        logger.info("Summary stored in memory.")

    def respond(self, user_input: str) -> str:
        logger.info(f"User asked: {user_input}")
        self.memory["chat_history"].append({"user": user_input})

        # Simple intent checks (expand as needed)
        if "what happened" in user_input.lower():
            response = self.memory["summary"]

        elif "vehicle" in user_input.lower():
            response = "Yes, vehicles were detected in the video. Would you like to see specific timestamps?"

        elif "timestamp" in user_input.lower() or "when" in user_input.lower():
            # Pull timestamps from summary
            summary = self.memory["summary"]
            times = [w for w in summary.split() if ":" in w]
            if times:
                response = f"Events occurred around: {', '.join(times)}"
            else:
                response = "No timestamps were found in the summary."

        else:
            response = "I'm still learning to understand that. You can ask me about detected events, vehicles, or timestamps."

        self.memory["chat_history"].append({"bot": response})
        return response
