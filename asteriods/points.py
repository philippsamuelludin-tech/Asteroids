import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

def start_points():
    Points_text = "Points: "
    points = "0"
    white = (255, 255, 255)
    green = (0, 255, 0)
    blue = (0, 0, 128)
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render((Points_text + points), green, white)
    textRect = text.get_rect()
    textRect.center = (100, 50)
    return points, text, textRect

def update_points(points):
    Points_text = "Points: "
    points = int(points) + 10
    points = str(points)
    
    white = (255, 255, 255)
    green = (0, 255, 0)
    blue = (0, 0, 128)
    font = pygame.font.Font('freesansbold.ttf', 20)
    text = font.render((Points_text + points), green, white)
    textRect = text.get_rect()
    textRect.center = (100, 50)
    return points, text, textRect

def asteroid_point(asteroid):
    Asteroid_text = "10"
    white = (255, 255, 255)
    green = (0, 255, 0)
    blue = (0, 0, 128)
    font = pygame.font.Font('freesansbold.ttf', 32)
    asteroid_text = font.render(Asteroid_text, green, white)
    textRect = asteroid_text.get_rect()
    textRect.center = (asteroid.position.x, asteroid.position.y)
    return asteroid_text, textRect

