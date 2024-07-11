#pip install pyttsx3
#pip install SpeechRecognition
#pip install PyAudio
#pip install randfacts

import pyttsx3 as p
import speech_recognition as sr
from selenium_web import *
from YT_audio import *
from news import *
import randfacts as rf
from jokes import *

#initiate pyttsx3 to convert text to speech
engine = p.init() #get information of current driver

#voice and speed of comp can be changed 

#speed
rate = engine.getProperty('rate')
#print(rate) #prints rate -- default is 200
#change property with setProperty()
#engine.setProperty('rate',130) #this made the speed slower
engine.setProperty('rate',180) #this made the speed faster/perfect

#voice
voices = engine.getProperty('voices')
#print(voices) #przints/returns list of two items -- two voices windows offers
#engine.setProperty('voices',voices[1].id) #male voice
engine.setProperty('voice',voices[1].id) #female voice -- change froom 'voices' to 'voice'

#everything we want computer to say something we use these two  lines of code -- can put it in function
#engine.say("hello there i am your voice assistant")
#engine.runAndWait()
def speak(text):
    engine.say(text)
    engine.runAndWait()

#CONVERT SPEECH TO TEXT
r = sr.Recognizer() #recognizer() helps retrieve audio from microphone

speak("Hello ma'am I'm your voice assistant. How are you?")

with sr.Microphone() as source: #Microphone is our source
    
    #background properties 
    r.energy_threshold=10000 #increases spectrum of voice -- inc. can even capture low voices
    r.adjust_for_ambient_noise(source,1.2) #cancels noises around you
    
    print("listening")  
    #CONVERSION -- main part --
    audio = r.listen(source) #make computer listen to us and store in audio var
    text = r.recognize_google(audio) #uses google api engine to convert audio to text
    print(text) #check the audio is converted to text
if "what" and "about" and "you" in text:
    speak("I am having a good day ma'am")
speak("what can i do for you?")

#Functionality/Automation 
#ex. search up something on wikipedia and show result
#use selenium webdriver - pip install selenium
with sr.Microphone() as source:
    #background properties 
    r.energy_threshold=10000 
    r.adjust_for_ambient_noise(source,1.2) 
    print("listening")
    audio = r.listen(source)
    text2 = r.recognize_google(audio)

if "information" in text2:
    speak("you need information related to which topic?")
    with sr.Microphone() as source:
        #background properties 
        r.energy_threshold=10000 
        r.adjust_for_ambient_noise(source,1.2) 
        print("listening")
        audio = r.listen(source)
        information = r.recognize_google(audio)
    speak("searching {} in wikipedia".format(information))
    assist = infow()
    speak(assist.get_info(information))
#YOUTUBE VIDEOS AND AUDIOS
elif "play" and ("video" or "music") in text2:
    speak("you want me to play which video?")
    with sr.Microphone() as source:
        #background properties 
        r.energy_threshold=10000 
        r.adjust_for_ambient_noise(source,1.2) 
        print("listening")
        audio = r.listen(source)
        song = r.recognize_google(audio)
    speak("Playing {} in youtube".format(song))
    assist = music()
    assist.play(song)
#NEWS
elif "news" in text2:
    speak("Sure ma'am, now i will read news for you.")
    #store content returned in list
    arr = news()
    for i in range(len(arr)):
        print(arr[i])
        speak(arr[i])
#RANDOM FACTS
elif "fact" or "facts" in text2:
#get random fact and store in x
    x = rf.get_fact()
    print(x)
    speak("Did you know that" + x )
#JOKES
elif "joke" or "jokes" in text2:
    speak("Sure sir, get ready for some chuckles")
    jokes = joke() #joke function returns list
    print(arr[0])
    speak(arr[0])
    print(arr[1])
    speak(arr[1])
#WEATHER + TIME
