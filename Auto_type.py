import speech_recognition as sr
r = sr.Recognizer()
try:
    with sr.Microphone(device_index=0) as source:
        print("listening ...")
        voice = r.record(source, duration=5)
        command = r.recognize_google(voice, language="en-in")
        print(command)
        print("Recognising....")
except:
    pass