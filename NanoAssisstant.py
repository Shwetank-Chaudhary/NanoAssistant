import threading
import speech_recognition as sr
import responses
import Text_to_speech as tts
import pygame
import pyaudio
import Visualizer

# INTIALIZING PYGAME

screen_ht = 700
screen_width = 960
pygame.init()
pygame.display.set_caption("Assisstant Visualiser")
screen = pygame.display.set_mode((screen_width, screen_ht))
clock = pygame.time.Clock()
icon = pygame.image.load("img.png")
pygame.display.set_icon(icon)

# PyAudio Intialization

chunk = 1024
Format = pyaudio.paInt16
channels = 1
rate = 44100

p = pyaudio.PyAudio()
stream = p.open(format = Format,
                channels=channels,
                frames_per_buffer=chunk,
                input=True,
                rate=rate)

def visualizer():
    amp = 100
    global running
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                exit()
        amp_adjustment = Visualizer.amplitude(stream,chunk) / 50
        amp = max(10, amp_adjustment)
        Visualizer.wave(amp, screen)
        clock.tick(60)
        pygame.display.update()


def Model():
    while running:
        try:
            with sr.Microphone() as source2:
                r.adjust_for_ambient_noise(source2, duration=0.2)
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

f1 = threading.Thread(target = visualizer, args=())
f2 = threading.Thread(target = Model, args=())
f1.start()
r = sr.Recognizer();
text = "Instructions to Use. If you want to stop the program just say STOP and it will stop the program."
tts.speak(text, rate=180)
f2.start()
f1.join(timeout=1)
f2.join(timeout=1)