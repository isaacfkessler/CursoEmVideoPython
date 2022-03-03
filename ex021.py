# BIBLIOTECA PYGAME PRECISA SER INSTALADA !!!!!
import pygame
# Inicializa o mixer PyGame
pygame.mixer.init()
# Inicializa o PyGame
pygame.init()

# Faz carregar a música
pygame.mixer.music.load('ex021.mp3')
# Põe a música para tocar
pygame.mixer.music.play()
# Faz o programa encerrar após a música acabar.
pygame.event.wait()