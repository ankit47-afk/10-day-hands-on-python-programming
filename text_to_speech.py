import pyttsx3

engine = pyttsx3.init()

text = "Hello Ankit, this is your text to speech tool."

engine.say(text)
engine.runAndWait()
