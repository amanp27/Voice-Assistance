import speech_recognition as sr
from dotenv import load_dotenv
import google.generativeai as genai
from gtts import gTTS
import playsound
from pydub import AudioSegment
import simpleaudio as sa
import os


load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")

r = sr.Recognizer()
mic = sr.Microphone()



while True:
    print("🎙️ बोलिए...")
    with mic as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        user_text = r.recognize_google(audio, language="hi-IN")
        print("🧑 Driver:", user_text)
    except Exception as e:
        print("⚠️ Error:", e)
        continue

    # Gemini response
    response = model.generate_content(user_text)
    bot_reply = response.text
    print("🤖 Bot:", bot_reply)

    # TTS playback (save as mp3 → convert to wav → play with simpleaudio)
    filename_mp3 = f"reply_{os.getpid()}.mp3"
    filename_wav = f"reply_{os.getpid()}.wav"

    tts = gTTS(text=bot_reply, lang="hi")
    tts.save(filename_mp3)

    # Convert mp3 → wav
    sound = AudioSegment.from_mp3(filename_mp3)
    sound.export(filename_wav, format="wav")

    # Play wav
    wave_obj = sa.WaveObject.from_wave_file(filename_wav)
    play_obj = wave_obj.play()
    play_obj.wait_done()

    # Cleanup
    os.remove(filename_mp3)
    os.remove(filename_wav)


    if "बाय" in user_text or "धन्यवाद" in user_text:
        break
