# 🎙️ Zero-Budget Voice-Activated AI Assistant

![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![Google Gemini](https://img.shields.io/badge/Powered%20by-Google%20Gemini-orange.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Open Source](https://img.shields.io/badge/Open%20Source-100%25-brightgreen.svg)

A completely free, lightweight, and fully functional voice-activated AI assistant built with Python. It listens to your voice, processes the query using Google's ultra-fast Gemini AI, and speaks back to you with a natural human-like voice using Google Text-to-Speech (gTTS).

No paid APIs, no heavy system requirements—just pure open-source magic! ✨

---

## 🏗️ How It Works



1. **Listen:** You speak into your microphone.
2. **Transcribe:** The `SpeechRecognition` library converts your audio into text.
3. **Think:** The text is sent to the Gemini API (`gemini-flash-lite-latest` model) to generate a smart, concise response.
4. **Speak:** `gTTS` converts the AI's text response back into an audio stream.
5. **Play:** `pygame` plays the audio seamlessly through your speakers without cluttering your system with audio files.

---

## 🚀 Features

* **🗣️ Hands-Free Interaction:** Fully voice-operated input and output.
* **🧠 Smart Brain:** Powered by the new `google-genai` SDK.
* **🔊 Natural Voice Output:** Uses `gTTS` for clear, native-sounding audio (includes Indian English accent support).
* **⚡ Seamless Playback:** Direct memory audio playback using `pygame` (no `.mp3` file saving required).
* **💸 100% Free:** Designed to run entirely on the generous free tier of Google AI Studio.
* **📊 Token Tracking:** Live tracking of API tokens used per conversation.

---

## 🛠️ Prerequisites

Before you begin, ensure you have the following:
* **Python 3.8+** installed on your machine.
* A working microphone and speaker setup.
* A **Free Gemini API Key** from [Google AI Studio](https://aistudio.google.com/).

---

## 💻 Step-by-Step Installation

Follow these instructions to get the project running on your local machine.

### Step 1: Clone the Repository
Open your terminal or command prompt and run:
```bash
git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
cd your-repo-name
Step 2: Install Dependencies
It is highly recommended to use the provided requirements.txt file to install the exact versions needed:

Bash
pip install -r requirements.txt
(Note for Windows users: If you face errors installing PyAudio, run pip install pipwin followed by pipwin install pyaudio.)

Step 3: Configure Your API Key
Open the main Python script (e.g., main.py).

Locate the API configuration line:

Python
client = genai.Client(api_key="YOUR_API_KEY") 
Replace "YOUR_API_KEY" with your actual API key from Google AI Studio. Do not share this key publicly!

▶️ Usage Guide
To start chatting with your AI assistant, run the script from your terminal:

Bash
python main.py
Wait for the console to display "Listening...".

Ask any question or give a command (e.g., "What is the speed of light?", "Tell me a joke").

The AI will process your request, print the token usage, and speak the answer out loud.

To exit the program, simply say: "Exit", "Stop", "Bye", or "Goodbye".

📁 Project Structure
Plaintext
📦 Your-Repo-Name
 ┣ 📜 main.py             # The core logic and main execution script
 ┣ 📜 requirements.txt    # List of Python dependencies
 ┣ 📜 .gitignore          # Tells Git which files to ignore (e.g., caches)
 ┗ 📜 README.md           # This documentation file
🤝 Contributing
Contributions, issues, and feature requests are always welcome! Feel free to check the issues page.
Fork the Project
Create your Feature Branch (git checkout -b feature/AmazingFeature)
Commit your Changes (git commit -m 'Add some AmazingFeature')
Push to the Branch (git push origin feature/AmazingFeature)
Open a Pull Request

📝 License
Distributed under the MIT License. See LICENSE for more information.

Built with ❤️ and Python.
