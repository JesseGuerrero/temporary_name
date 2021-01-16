from sam import AudioRecognition

print("How may i help you?")
audio_data = AudioRecognition.get_audio()
AudioRecognition.respond(audio_data)