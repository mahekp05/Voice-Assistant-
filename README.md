# 🎙️ Luna – Python Voice Assistant

Luna is a lightweight, Python-based voice assistant designed to perform everyday tasks using speech commands. With over 80% speech recognition accuracy, Luna helps users automate routine web actions like checking the news, searching Wikipedia, or playing music — all hands-free.

---

## 🚀 Overview

This project was built to explore the intersection of speech interfaces and automation. Luna uses natural language input to trigger system and web-based actions through speech recognition and Python scripting.

---

## 🎯 Key Features

- 🗣️ Voice-controlled search for Wikipedia, YouTube, and Google
- 🌤️ Real-time weather updates
- 📰 Fetches and reads news headlines aloud
- 😂 Tells random jokes and fun facts
- 🎵 Plays YouTube music automatically
- 🧠 Personalized experience via simple keyword-based NLP

---

## 🧾 File Descriptions

| File               | Description                                      |
|--------------------|--------------------------------------------------|
| `main.py`          | Entry point for the assistant                    |
| `yt_audio.py`      | Handles YouTube audio search and playback        |
| `jokes.py`         | Returns jokes and fun facts                      |
| `news.py`          | Pulls current news headlines                     |
| `selenium_web.py`  | Automates search and interaction using Selenium  |
| `weather_time.py`  | Fetches weather and time updates                 |
| `ss.py` / `errors` | Logs and error handling modules                  |
| `README.md`        | Project documentation                            |

---

## 🛠 Tech Stack

- `Python`
- `SpeechRecognition`
- `Pyttsx3`
- `Selenium`
- `Requests`
- `BeautifulSoup4`

---

## ▶️ How to Run Luna

1. **Clone the repository**
git clone https://github.com/mahekp05/voice-assistant
cd voice-assistant

Install dependencies
pip install pyttsx3 SpeechRecognition pyaudio selenium requests beautifulsoup4 wikipedia pywhatkit python-dotenv

Run the assistant
python main.py
