import speech_recognition as sr
import time
from datetime import date, datetime
import webbrowser
import os
import playsound
from gtts import gTTS
import random


rec = sr.Recognizer()
mic = sr.Microphone()

def get_audio():
    with mic as source:
        rec.adjust_for_ambient_noise(source)
        audio = rec.listen(source)
        voice_input = ''
        try:
            voice_input = rec.recognize_google(audio)
        except sr.UnknownValueError:
            speak("Sorry, I did not get that.")
        except sr.RequestError:
            speak("Sorry, API currently unavailable.")
        return voice_input

def response(voice_input):
    if "your name" in voice_input:
        speak("My name is Biri")
    elif ("hello" in voice_input) or ("hi" in voice_input):
        speak("Hello!")
    elif "how are you" in voice_input:
        speak("I'm fine, thank you. How are you?")
    elif ("what day" in voice_input) or ("date" in voice_input):
        today = date.today()
        day = today.strftime("%B %d, %Y")
        speak("The date today is " + day)
    elif ("time" in voice_input) or ("what is the time" in voice_input):
        now = datetime.now()
        time_string = now.strftime("%H:%M:%S")
        speak("The time is " + time_string)
    elif "search" in voice_input:
        speak("What do you want me to search?")
        voice_input = get_audio()
        if voice_input != '':
            query = voice_input.replace(' ', '+')
            url = 'https://google.com/search?q=' + query
            webbrowser.get().open(url)
            speak("This is what I found for " + voice_input)
    elif ("map" in voice_input) or ("Google Maps" in voice_input) or ("location" in voice_input):
        speak("What place do you want me to search?")
        voice_input = get_audio()
        if voice_input != '':
            query = voice_input.replace(' ', '+')
            url = 'https://google.ca/maps/place/' + query
            webbrowser.get().open(url)
            speak("I found " + voice_input)
    elif ("exit" in voice_input) or ("quit" in voice_input):
        exit()
    else:
        speak("Sorry, I did not understand. Could you please repeat that?")

def speak(voice_input):
    print(voice_input)
    tts = gTTS(text=voice_input, lang='en')
    r = random.randint(1, 10000);
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    os.remove(audio_file)

time.sleep(1)
speak("What can I help you with?")
while 1:
    voice_input = get_audio()
    if voice_input != '':
        response(voice_input)