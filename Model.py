import speech_recognition as sr
import responses
import Text_to_speech as tts


r = sr.Recognizer();
text = "Instructions to Use. If you want to stop the program just say STOP and it will stop the program."
tts.speak(text, rate=180)

while True:
    try:
        with sr.Microphone() as source2:
            r.adjust_for_ambient_noise(source2,duration=0.2)
            tts.speak("You may speak now ")
            print("Listening.....")
            audio = r.listen(source2, timeout=3)
            myText = r.recognize_google(audio)
            print(myText)
            mText = myText.lower()
            if 'stop' in myText:
                tts.speak("Program has been terminated. Thank your for you patience.", rate=180)
                break
            answer = responses.get_response(myText)
            print("Response: ", answer)
            if answer is None:
                tts.speak("Did Not Get an Answer. Please Try Again")
            else:
                tts.speak(answer)
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
    except sr.UnknownValueError:
        print("unknown Error Occured")

