from pyaudio import PyAudio

def choose_device() -> int: #returns an int
    print("Choose a device: ")
    audio = PyAudio()

    #prints available devices
    numOfDevices = PyAudio.get_device_count(audio)
    for index in range(0, numOfDevices):
        audioInfo = PyAudio.get_device_info_by_index(audio, index)
        print(str(audioInfo.get('index')) + ": " + audioInfo.get('name'))
    return int(input("Choose device: "))