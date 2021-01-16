import speech_recognition as sr
import pyaudio as pa
import webbrowser
'''
Handles all speech recognition
'''
speechRecognizer = sr.Recognizer()

'''
adjust_for_ambient_noise allows for microphones with automatic noise reduction to function.
'''
def get_audio() -> str:
    with sr.Microphone() as source: # source of our audio
        speechRecognizer.adjust_for_ambient_noise(source, duration=1)
        audio = speechRecognizer.listen(source) # it is a listener for the recogniser
        audio_load = ' '
        try:
            audio_load = speechRecognizer.recognize_google(audio) # to convert the audio to text
        except sr.UnknownValueError:
            print("Sorry, I did not get that")
        except sr.RequestError:
            print("Server Down, Try again later")
        print(audio_load)
    return audio_load

def respond(audio_data):
    if 'what is your name' in audio_data:
        print ('my name is Sam')
    if 'how are you' in audio_data:
        print("I'm fine")
    if 'search' in audio_data:
        s = get_audio("What do you wanna search for")
        url = f"https://www.google.com/search?q={s}"
        webbrowser.get().open(url)