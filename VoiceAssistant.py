import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import os

# === Speech Engine Setup ===
engine = pyttsx3.init()
engine.setProperty("rate", 170)  # speaking speed

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio).lower()
        print(f"👉 You said: {command}")
        return command
    except sr.UnknownValueError:
        speak("Sorry, I didn’t catch that.")
        return ""
    except sr.RequestError:
        speak("Network error. Try again later.")
        return ""

# === Commands ===
def run_assistant():
    speak("Hey! How can I help?")
    command = listen()

    if "time" in command:
        now = datetime.datetime.now().strftime("%H:%M")
        speak(f"The time is {now}")

    elif "open youtube" in command:
        webbrowser.open("https://youtube.com")
        speak("Opening YouTube")

    elif "open google" in command:
        webbrowser.open("https://google.com")
        speak("Opening Google")

    elif "play music" in command:
        music_dir = "C:/Users/Public/Music"  # change to your music folder
        songs = os.listdir(music_dir)
        if songs:
            os.startfile(os.path.join(music_dir, songs[0]))
            speak("Playing music")
        else:
            speak("No music found in your folder")

    elif "stop" in command or "quit" in command:
        speak("Goodbye!")
        exit()

    else:
        speak("I don’t know that one yet.")

# === Main Loop ===
while True:
    run_assistant()
