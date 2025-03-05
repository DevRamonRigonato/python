import pygame
import time
pygame.mixer.init()
pygame.mixer.music.load('ex014.mp3')
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    time.sleep(1)  