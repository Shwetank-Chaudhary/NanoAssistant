import speech_recognition as sr

r = sr.Recognizer()
print("Starting.....")

while(1):
    try:
        with sr.Microphone() as source2:
            r.adjust_for_ambient_noise(source2, duration=0.2)
            audio = r.listen(source2)
            MyText = r.recognize_google(audio)
            MyText = MyText.lower()
            if 'quit' in MyText:
                print("Bye")
                break
            print("You Said: ", MyText)
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
    except sr.UnknownValueError:
        print("unknown Error Occured")