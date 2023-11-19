import googletrans
import speech_recognition as sr
import gtts
import playsound

recognizer = sr.Recognizer()
translator = googletrans.Translator()
input_lang = 'hi-IN'
output_lang = 'en'
try:
    with sr.Microphone() as source:
        print('Speak Now')
        voice = recognizer.record(source, duration=5)
        text = recognizer.recognize_google(voice, language=input_lang)
        print(text)
except:
    pass

translated = translator.translate(text, dest=output_lang)
print(translated.text)
converted_audio = gtts.gTTS(translated.text, lang=output_lang)
converted_audio.save('output.mp3')
playsound.playsound('output.mp3')
#print(googletrans.LANGUAGES)