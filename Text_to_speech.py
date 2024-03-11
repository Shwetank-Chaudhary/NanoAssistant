import pyttsx3

def speak(message,volume=1,rate = 125):
    engine = pyttsx3.init()
    engine.setProperty('volume', volume)
    engine.setProperty('rate', rate)
    voice = engine.getProperty('voices')
    engine.setProperty('voice', voice[1].id)
    engine.say(message)
    engine.runAndWait()



# engine = pyttsx3.init()
# engine.say("Hello Baby!!")
# engine.runAndWait()
#
# '''RATE'''
# rate = engine.getProperty('rate')
# print("Rate of my speech is: ", rate)
# engine.setProperty('rate', 125)
# engine.say("Hello Baby!!")
# engine.runAndWait()
#
# '''Volume'''
# volume = engine.getProperty('volume')
# print("Volume: ", volume)
# engine.setProperty('volume', 1)
# engine.say("Hello Baby!!")
# engine.runAndWait()
#
# '''VOICE'''
# voice = engine.getProperty('voices')
# engine.setProperty('voice', voice[1].id)    #1 for Female Voice and 0 for Male Voice
# engine.say("Hello Baby!!")
# engine.runAndWait()