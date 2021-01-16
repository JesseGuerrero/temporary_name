import speech_recognition as sr
import webbrowser
import playsound
import os
import random
from gtts import gTTS
'''
Handles all speech recognition
'''
speechRecognizer = sr.Recognizer()

'''
adjust_for_ambient_noise allows for microphones with automatic noise reduction to function.
'''
def get_audio(ask = False):
    with sr.Microphone() as source: # source of our audio
        if(ask):
            sam_speak(ask)
        # speechRecognizer.adjust_for_ambient_noise(source, duration=1)
        audio = speechRecognizer.listen(source) # it is a listener for the recogniser
        audio_load = ' '
        try:
            audio_load = speechRecognizer.recognize_google(audio) # to convert the audio to text
        except sr.UnknownValueError:
            sam_speak("Sorry, I did not get that")
        except sr.RequestError:
            sam_speak("Server Down, Try again later")
        # print(audio_load)
    return audio_load


def sam_speak(audio):
    tts = gTTS(text=audio,lang='en')
    r = random.randint(1,100000)
    audio_file = 'audio-'+str(r)+'.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio)
    os.remove(audio_file)


def respond(audio_data):
    if 'what is your name' in audio_data:
        sam_speak('my name is Sam')
    if 'how are you' in audio_data:
        sam_speak("I'm fine")
    if 'search' in audio_data:
        s = get_audio("What do you wanna search for?")
        url = f"https://www.google.com/search?q={s}"
        webbrowser.get().open(url)
        sam_speak("here are the results for"+s)
    if 'location' in audio_data:
        s = get_audio("what place do you wanna look for?")
        url = f"https://www.google.nl/maps/place/{s}/&amp;"
        webbrowser.get().open(url)
        sam_speak("Here are the result for the location "+s)
    if 'exit' in audio_data:
        exit()



sam_speak("How can i help you?")
audio_data = get_audio()
respond(audio_data)