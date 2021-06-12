import speech_recognition as stt

with stt.Microphone() as source:
    help(r.listen(source))