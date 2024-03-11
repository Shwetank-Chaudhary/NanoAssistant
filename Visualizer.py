import pygame
import pyaudio
import math
"""# INTIALIZING PYGAME

screen_ht = 700
screen_width = 960
pygame.init()
pygame.display.set_caption("Assisstant Visualiser")
screen = pygame.display.set_mode((screen_width, screen_ht))
clock = pygame.time.Clock()
icon = pygame.image.load("img.png")
pygame.display.set_icon(icon)

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render("Listening...", True, green, blue)
textRect = text.get_rect()
# set the center of the rectangular object.
textRect.center = (screen_width - 100, screen_ht - 64)


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

def _screen():
    return screen"""


def amplitude(stream,chunk):
    data = stream.read(chunk)
    rms = 0
    for i in range(0,len(data),2):
        sample = int.from_bytes(data[i:i+2], byteorder='little', signed=True)
        rms += sample*sample
    rms = math.sqrt(rms * 2 / chunk)
    return rms

def wave(loudness, screen, screen_width=960, screen_ht=720):
    points = []
    screen.fill((loudness%255,0,0))
    if loudness > 10:
        for x in range(screen_width):
            y = screen_ht/2 + int(loudness * math.sin(x*0.02))
            points.append((x, y))
    else:
        points.append((0, screen_ht/2))
        points.append((screen_width, screen_ht/2))
    pygame.draw.lines(screen, (255, 255, 255), False, points, 4)
    pygame.display.flip()



'''##Visualiser
def visualizer():
    running = True
    amp = 100
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        amp_adjustment = amplitude()/50
        amp = max(10, amp_adjustment)
        wave(amp)
        # screen.fill((0 + red, 255 - red, 0))  # RGB

        # screen.blit(text,textRect)
        clock.tick(60)
        pygame.display.update()

    pygame.quit()
'''
'''#Fonts
font = pygame.font.get_fonts()
print(font)'''
