from vosk import Model, KaldiRecognizer
import pyaudio
import json  # Import the json module to parse the JSON result
import pyttsx3
import time
import pywhatkit

query = "Music"

def talk(command):
    engine = pyttsx3.init()
    voice =engine.getProperty('voices')
    engine.setProperty('voice',voice[1].id)
    engine.say(command)
    engine.runAndWait()


model = Model("/vosk-model-small-en-us-0.15")
recognizer = KaldiRecognizer(model, 44100)

mic = pyaudio.PyAudio()
stream = mic.open(rate=44100, channels=1, format=pyaudio.paInt16,
                  input=True, frames_per_buffer=1024)
stream.start_stream()



def search(duration_seconds):
    start_time = time.time()
    talk("say now...")

    while time.time() - start_time < duration_seconds:
        data = stream.read(1024)
        if recognizer.AcceptWaveform(data):
            result = json.loads(recognizer.Result())
            query = result["text"]
            print(query)
            pywhatkit.playonyt(query)
            talk(f"playing {query}")

# Specify the desired duration in seconds
search_duration = 10  # Example: run for 60 seconds

search(search_duration)
