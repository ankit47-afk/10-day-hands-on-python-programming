
import pyttsx3 # it is used for text to speech conversion
import speech_recognition as sr
import webbrowser # it is used to open web browsers
import os # it is used to interact with the operating system
import pywhatkit # it is used to send whatsapp messages
import subprocess # it is used to run system commands

speaker = pyttsx3.init()
mic = sr.Recognizer()

def open_whatsapp():
    """Open WhatsApp web"""
    speaker.say("Opening WhatsApp")
    speaker.runAndWait()
    webbrowser.open("https://web.whatsapp.com")
    print("Opening WhatsApp Web...")

def open_browser():
    """Open default browser"""
    speaker.say("Opening browser")
    speaker.runAndWait()
    webbrowser.open("https://www.google.com")
    print("Opening Google...")

def open_whatsapp_desktop():
    """Open WhatsApp desktop app"""
    speaker.say("Opening WhatsApp desktop")
    speaker.runAndWait()
    try:
        subprocess.Popen(r"C:\Users\ankit\AppData\Local\WhatsApp\WhatsApp.exe")
        print("Opening WhatsApp Desktop...")
    except FileNotFoundError:
        print("WhatsApp Desktop not found. Opening web version.")
        open_whatsapp()

speaker.say("Welcome to Jarvis")
speaker.runAndWait()
speaker.stop()  # Properly stop the engine to avoid cleanup errors

with sr.Microphone() as source:
    mic.adjust_for_ambient_noise(source, duration=1)
    print("Listening... Say 'open notepad' or 'exit'")
    while True:
        try:
            print("Start Speaking...")
            audio = mic.listen(source, timeout=5, phrase_time_limit=6)
            text = mic.recognize_google(audio)
            print("You said:", text)
        except sr.WaitTimeoutError:
            # no speech detected within timeout, continue listening
            continue
        except sr.UnknownValueError:
            print("Could not understand audio")
            continue
        except sr.RequestError as e:
            print("Recognition error:", e)
            break

        text_lower = text.lower()

        if "open notepad" in text_lower:
            speaker.say("Opening Notepad")
            speaker.runAndWait()
            print("Opening Notepad...")
            try:
                # Try a direct startfile first (Windows)
                os.startfile("notepad.exe")
            except Exception:
                # Fallback to subprocess if needed
                import subprocess
                subprocess.Popen(["notepad.exe"])
        elif "open whatsapp" in text_lower:
            open_whatsapp_desktop()
        elif "open browser" in text_lower:
            open_browser()
        elif "send message" in text_lower:
            print("Sending MSG...")
            speaker.say("Sending message")
            speaker.runAndWait()
            pywhatkit.sendwhatmsg_instantly("+91", "Hi I am from VGU")
        elif any(k in text_lower for k in ("exit", "quit", "stop")):
            speaker.say("Goodbye")
            speaker.runAndWait()
            break