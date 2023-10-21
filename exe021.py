# Exercício Python #021 - Tocando um MP3
import pygame

try:
    pygame.init()
    pygame.mixer.music.load("exemplo.mp3")
    pygame.mixer.music.play()
    input()
finally:
    pygame.mixer.music.stop()
    pygame.mixer.quit()