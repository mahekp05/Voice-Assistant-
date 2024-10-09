# pip install pyttsx3
# pip install SpeechRecognition
# pip install PyAudio
# pip install randfacts

import pyttsx3 as p
import speech_recognition as sr
from selenium_web import *
from YT_audio import *
from news import *
import randfacts as rf
from jokes import *

# Initialize pyttsx3 to convert text to speech
engine = p.init()

# Set voice and speed properties
engine.setProperty('rate', 180)  # Set speech speed
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Set to female voice

# Function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Initialize speech recognition
r = sr.Recognizer()

# Function to capture and recognize speech from the microphone
def listen_from_mic():
    with sr.Microphone() as source:
        # Set background noise and energy threshold properties
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        
        print("Listening...")
        audio = r.listen(source)  # Capture audio from microphone
        
        try:
            text = r.recognize_google(audio)  # Convert audio to text using Google API
            print(f"Recognized: {text}")  # Display the recognized text
            return text
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
            return None
        except sr.RequestError:
            print("Sorry, there was an issue with the Google API.")
            return None

# Welcome message from the assistant
speak("Hello ma'am, I am Luna, your voice assistant today. How are you?")

# Listen for the first response
text = listen_from_mic()

if text and "what" in text and "about" in text and "you" in text:
    speak("I am having a good day ma'am")
speak("What can I do for you?")

# Main functionality/Automation
text2 = listen_from_mic()

if text2:
    # Wikipedia search functionality
    if "information" in text2:
        speak("You need information related to which topic?")
        information = listen_from_mic()
        if information:
            speak(f"Searching {information} in Wikipedia")
            assist = infow()
            result = assist.get_info(information)
            if result:
                speak(result)
            assist.close_driver()

    # YouTube video or music playback
    elif "play" in text2 and ("video" in text2 or "music" in text2):
        speak("You want me to play which video?")
        song = listen_from_mic()
        if song:
            speak(f"Playing {song} on YouTube")
            assist = music()
            assist.play(song)

    # News reading functionality
    elif "news" in text2:
        speak("Sure ma'am, now I will read the news for you.")
        news_list = news()  # Fetch news in list form
        for item in news_list:
            print(item)
            speak(item)

    # Random facts functionality
    elif "fact" in text2 or "facts" in text2:
        fact = rf.get_fact()  # Fetch a random fact
        print(fact)
        speak(f"Did you know that {fact}")

    # Jokes functionality
    elif "joke" in text2 or "jokes" in text2:
        speak("Sure sir, get ready for some chuckles")
        joke_list = joke()  # Fetch jokes in list form
        print(joke_list[0])
        speak(joke_list[0])
        print(joke_list[1])
        speak(joke_list[1])

    # Placeholder for future weather or time functionality

