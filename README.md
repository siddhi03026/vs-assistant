# vs-assistant


# 👁️ Visual Understanding Chat Assistant

A production-ready prototype of a Visual Understanding AI Assistant that can summarize video content and support intelligent conversations based on visual events. Ideal for use cases like traffic monitoring, behavioral analysis, and security compliance.

---

## 🔍 Overview

The Visual Understanding Chat Assistant allows users to upload videos or provide video links, then processes them to extract key frames, simulate event detection, and generate natural language summaries. It also includes a conversational agent to interact with these summaries.

---

## ✨ Core Features

- **🎬 Video Upload & Processing**  
  Upload `.mp4` videos or use video links. Frames are extracted and analyzed using OpenCV.

- **🧠 Event Recognition**  
  Simulated rule-based detection of visual events (e.g., movement, behavior violations). Ready for YOLO integration.

- **📝 Automated Summarization**  
  Generates text summaries of detected events. Supports GPT/OpenAI for advanced summarization.

- **💬 Multi-Turn Conversational Assistant**  
  Built-in memory for contextual conversations. Ask follow-up questions based on visual data.

- **🕸️ Web Interface**  
  Simple HTML/JavaScript UI to upload videos, view summaries, and chat with the assistant.

---

## ⚙️ Tech Stack

- **FastAPI** — REST API Framework  
- **OpenCV** — Frame extraction and video analysis  
- **Loguru** — Advanced logging  
- **JavaScript + HTML** — Frontend  
- **Uvicorn** — ASGI server  
- **(Optional)** OpenAI GPT or LangChain for smarter summaries

---

## 🗂️ Project Structure

```
visual_assistant/
├── main.py                  # FastAPI App Entry
├── utils/
│   ├── video_processor.py   # Video frame extraction & detection
│   ├── summarizer.py        # Event summarization logic
│   └── chat_handler.py      # Chat assistant with memory
├── templates/
│   └── index.html           # Frontend interface
├── static/
│   └── script.js            # JS for chat and upload
├── uploads/                 # Stores uploaded video files
├── requirements.txt         # Python dependencies
└── README.md                # Project description
```

---

## 🚀 Getting Started

1. **Clone the repository**
```bash
git clone https://github.com/siddhi03026/vs-assistant.git
cd visual-chat-assistant
```

2. **Create a virtual environment & activate it**
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/macOS
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run the server**
```bash
uvicorn main:app --reload
```

5. **Open your browser**
```
http://localhost:8000
```

---

## 🧪 Sample Use Cases

- 🚦 "What happened at the traffic light between 00:30 and 01:00?"
- 🚶 "Were any pedestrians detected in the crosswalk?"
- 📋 "Summarize all rule violations from the video."

---

## 🔮 Future Enhancements

- ✅ Integrate YOLOv5/YOLOv8 for object detection  
- ✅ Export results as PDF/CSV reports  
- ✅ Add voice input/output for hands-free interaction  
- ✅ Extend to real-time camera streaming

---

## 📄 License

MIT License — free for personal and commercial use with proper attribution.

---

## 🙌 Acknowledgments

Built using OpenAI, FastAPI, and the power of computer vision. Special thanks to the open-source community.

