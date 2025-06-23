import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Listening...")
    audio = r.listen(source)

try:
    command = r.recognize_google(audio)
    print(f"You said: {command}")
except:
    print("Sorry, I couldn't understand.")

