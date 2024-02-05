import os
import speech_recognition as sr
from playsound import playsound
import threading


def play_audio(file_path):
    playsound(file_path)


def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  
        audio = recognizer.listen(source)  

    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio)  
        return command.lower()
    except sr.UnknownValueError:
        print("Sorry, could not understand audio.")
        return None
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        return None


def main():
    
    file_path = "raone.mp3"
    

    if os.path.exists(file_path):
        while True:
            command = recognize_speech()
            if command == "start":
                audio_thread = threading.Thread(target=play_audio, args=(file_path,))
                audio_thread.start()
            elif command == "stop":
                print("Stopping playback.")
                break
    else:
        print("Error: The specified file does not exist.")

if __name__ == "__main__":
    main()



