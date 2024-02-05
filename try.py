import speech_recognition as sr

# Initialize recognizer
recognizer = sr.Recognizer()

# Function to recognize speech from an audio file
def recognize_speech_from_file(file_path):
    with sr.AudioFile(file_path) as source:
        audio_data = recognizer.record(source)  # Read the entire audio file

    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio_data)  # Recognize speech using Google Web Speech API
        return text
    except sr.UnknownValueError:
        print("Sorry, could not understand audio.")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

# Main function
def main():
    file_path = input("Enter the path to the uploaded audio file: ")
    recognized_text = recognize_speech_from_file(file_path)
    if recognized_text:
        print("Recognized text:", recognized_text)

if __name__ == "__main__":
    main()
