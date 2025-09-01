# Hindi Voice Assistant – Ola Support Bot
This is a voice-based AI assistant built in Python.
It listens to the driver’s voice in Hindi, sends the query to Google’s Gemini 1.5 Flash model, and responds back in Hindi speech using gTTS (Text-to-Speech).

Example interactions:

    * Driver: मुझे ओला के बारे में बताइए
    
    * Driver: ओला में कैब कैसे बुक करें?

## 📌 Features
* Speech-to-Text (STT) using speech_recognition (Google API).

* AI Responses powered by Google Gemini 1.5 Flash.

* Text-to-Speech (TTS) in Hindi using gTTS.

* Temporary audio files are auto-deleted after playback.

<!-- * Interactive loop – keeps listening until user says "बाय" or "धन्यवाद". -->


## 🛠️ Prerequisites & Learning Journey

This assessment was very new to me.
Before directly jumping into coding, I first learned and experimented with the following tools:

* LiveKit → for real-time audio streaming.

* gTTS → convert text replies into Hindi speech.

* pydub → handle MP3 → WAV conversions.

* simpleaudio → play audio seamlessly.

* .env + dotenv → securely load API keys.

I am confident that with time and practice, I can make this project production-ready. 🚀

## ⚙️ Setup Instructions
1. Clone the Repository
```
git clone https://github.com/<your-username>/hindi-voice-assistant.git
cd hindi-voice-assistant
```

2. Create Virtual Environment
```
python -m venv voice
voice\Scripts\activate   # On Windows
```

3. Install Dependencies
```     
pip install -r requirements.txt
```

## 📂 File Structure
```
├── agent.py        # Main code
├── .env             # API key storage
├── requirements.txt # Dependencies
└── README.md        # Project documentation
```

## 📌 Notes

Replies are temporarily saved as audio files before playback. These files are auto-deleted after speaking.

You can improve further by making playback real-time without saving files.

This is a first version, built to demonstrate understanding of speech recognition + AI responses + speech synthesis.
