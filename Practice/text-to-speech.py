## *HOW TO RUN THIS PROGRAM*
##cd ~/Desktop/python
##python3 -m venv venv
##source venv/bin/activate
##pip install pyttsx3
##python text-to-speech.py

import pyttsx3

engine = pyttsx3.init()

print("Text-to-Speech")
print("Type 'quit' to exit.")

while True:
    text = input("Enter text: ")

    if text.lower() == "quit":
        break

    engine.say(text)
    engine.runAndWait()

