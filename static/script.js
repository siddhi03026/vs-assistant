const uploadForm = document.getElementById("upload-form");
const summarySection = document.getElementById("summary-section");
const summaryText = document.getElementById("summary-text");
const chatSection = document.getElementById("chat-section");
const chatBox = document.getElementById("chat-box");
const userInput = document.getElementById("user-input");

uploadForm.addEventListener("submit", async function (e) {
    e.preventDefault();
    
    const fileInput = document.getElementById("video-file");
    const file = fileInput.files[0];
    const formData = new FormData();
    formData.append("file", file);

    const response = await fetch("/upload/", {
        method: "POST",
        body: formData,
    });

    const data = await response.json();
    summaryText.textContent = data.summary;
    summarySection.style.display = "block";
    chatSection.style.display = "block";
    chatBox.innerHTML = ""; // Clear previous chats
});

async function sendMessage() {
    const message = userInput.value.trim();
    if (!message) return;

    appendMessage("user", message);
    userInput.value = "";

    const response = await fetch("/chat/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message }),
    });

    const data = await response.json();
    appendMessage("bot", data.response);
}

function appendMessage(sender, text) {
    const msgDiv = document.createElement("div");
    msgDiv.className = "message";
    msgDiv.innerHTML = `<span class="${sender}">${sender === "user" ? "You" : "Assistant"}:</span> ${text}`;
    chatBox.appendChild(msgDiv);
    chatBox.scrollTop = chatBox.scrollHeight;
}
