import pygame
from constants import *

def start_lives():
    Lives_text = "Lives: "
    lives = str(PLAYER_LIVES)
    white = (255, 255, 255)    
    green = (0, 255, 0)
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render((Lives_text + lives), True, white)
    textRect = text.get_rect()
    textRect.center = (1200, 50)
    return lives, text, textRect


def update_lives(lives):
    Lives_text = "Lives: "
    lives = str(int(lives) - 1)
    white = (255, 255, 255)
    green = (0, 255, 0)
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render((Lives_text + lives), True, white)
    textRect = text.get_rect()
    textRect.center = (1200, 50)
    return lives, text, textRect