import speech_recognition as sr
import webbrowser

r = sr.Recognizer()

def get_audio(ask = False): #ask is a optional argument
    with sr.Microphone() as source: # source of our audio
        if ask:
            print(ask)
        audio = r.listen(source) # it is a listener for the recogniser
        audio_load = ' '
        try:
            audio_load = r.recognize_google(audio) # to convert the audio to text
        except sr.UnknownValueError:
            print("Sorry, I did not get that")
        except sr.RequestError:
            print("Server Down, Try again later")
    return audio_load

def respond(audio_data):
    if 'what is your name' in audio_data:
        print ('my name is Sam .')
    if 'how are you' in audio_data:
        print("I'm fine")
    if 'search' in audio_data:
        s = get_audio("What do you wanna search for")
        url = f"https://www.google.com/search?q={s}"
        webbrowser.get().open(url)


print("How may i help you?")
audio_data = get_audio()
respond(audio_data)
