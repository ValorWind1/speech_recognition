import speech_recognition as speech

sp = speech.Recognizer()

with speech.Microphone() as source:
    print("Speak now: ")
    audio = sp.listen(source)
    try:
        text = sp.recognize_google(audio)
        print("What You said is: {]".format(text))
    except:
        print("sorry couldn't understand what you said")
