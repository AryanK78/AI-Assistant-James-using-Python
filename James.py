import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import requests


recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsAPI = "53d4a660b71844b6b95be2131814a9ed"

def speak(text):
    engine.say(text)
    engine.runAndWait()

# def speak(text):
#     tts = gTTS('hello')
#     tts.save('hello.mp3')


    # # Step 1: Create the MP3 file using gTTS
    # text = "Hello, this is a test message."
    # language = 'en'
    # output_file = "new_output.mp3"  # Changed file name

    # # Generate the MP3 file
    # tts = gTTS(text=text, lang=language, slow=False)
    # tts.save(output_file)

    # # Step 2: Initialize Pygame mixer and play the MP3 file
    # pygame.mixer.init()

    # # Load the MP3 file
    # pygame.mixer.music.load(output_file)

    # # Play the MP3 file
    # pygame.mixer.music.play()

    # # Keep the program running until the sound finishes playing
    # while pygame.mixer.music.get_busy():  # This will check if the music is still playing
    #     time.sleep(1)  # Sleep for a second to avoid consuming too much CPU



def processCommand(c):
    c = c.lower().replace("play ", "").strip()  # Normalize the command
    print(f"Processed command for query: {c}")
    
    if "open google" in c:
        webbrowser.open("http://google.com")
    elif "open my channel" in c:
        webbrowser.open("https://www.youtube.com/@ArbazGad")
    elif "open my instagram profile" in c:
        webbrowser.open("https://www.instagram.com/wandermelon_/")

    # Adding news through NewsApi
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsAPI}")
        data = r.json()

        # Check if the request was successful
        if data["status"] == "ok":
    # Extract and print the headlines of the top articles
            articles = data["articles"]
            for i, article in enumerate(articles, 1):
                speak(f"{i}. {article['title']}")
                

    elif c in musiclibrary.music:
        link = musiclibrary.music[c]
        speak(f"Playing {c}")
        webbrowser.open(link)
    else:
        speak(f"Sorry, I couldn't find the song '{c}'.")









if __name__ == "__main__":
    speak("James starting....") 
    while True:
        print("Recognizing")
        try:
            with sr.Microphone() as source:
                print("Listening for wake word...")
                audio = recognizer.listen(source, timeout=2, phrase_time_limit=1)
            word = recognizer.recognize_google(audio).lower()
            print(f"Wake word recognized: {word}")
            
            if word == "james":
                speak("Yes")
                with sr.Microphone() as source:
                    print("Listening for command...")
                    audio = recognizer.listen(source)
                    command = recognizer.recognize_google(audio)
                    # print(f"Command recognized: {command}")
                    processCommand(command)
        except Exception as e:
            print(f"Error: {e}")


#New Code: 



# Initialize the recognizer and text-to-speech engine
