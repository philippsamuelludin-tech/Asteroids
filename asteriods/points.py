import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
import random


class FloatingText:
    def __init__(self, text, x, y, duration=90):  # ~1.5s at 60fps
        self.x = x
        self.y = y
        self.duration = duration
        self.timer = 0
        self.alive = True
        white = (255, 255, 255)
        green = (0, 255, 0)
        font = pygame.font.Font('freesansbold.ttf', 20)
        self.surface = font.render(text, True, white)
        self.rect = self.surface.get_rect(center=(x, y))

    def update(self):
        self.timer += 1
        self.y -= 0.5  # drift upward
        self.rect.center = (self.x, self.y)
        if self.timer >= self.duration:
            self.alive = False

    def draw(self, screen):
        # Fade out in the last 30 frames
        if self.timer > self.duration - 30:
            alpha = int(255 * (self.duration - self.timer) / 30)
        else:
            alpha = 255
        temp_surface = self.surface.copy()
        temp_surface.set_alpha(alpha)
        screen.blit(temp_surface, self.rect)


def start_points():
    Points_text = "Points: "
    points = "0"
    white = (255, 255, 255)
    green = (0, 255, 0)
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render((Points_text + points), True, white)
    textRect = text.get_rect()
    textRect.center = (100, 50)
    return points, text, textRect


def update_points(points):
    Points_text = "Points: "
    points = str(int(points) + 10)
    white = (255, 255, 255)
    green = (0, 255, 0)
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render((Points_text + points), True, white)
    textRect = text.get_rect()
    textRect.center = (100, 50)
    return points, text, textRect


def asteroid_point(asteroid):
    return FloatingText("+10", asteroid.position.x, asteroid.position.y, duration=30)

class Particle(FloatingText):
    def __init__(self, x, y):
        super().__init__("", x, y, duration=30)
        self.velocity = pygame.Vector2(random.uniform(-2, 2), random.uniform(-2, 2))
        self.surface = pygame.Surface((4, 4))
        self.surface.fill((255, 165, 0))  # Yellow particles
        self.rect = self.surface.get_rect(center=(x, y))

    def update(self):
        super().update()
        self.x += self.velocity.x
        self.y += self.velocity.y
        self.rect.center = (self.x, self.y)

    def draw(self, screen):
        # Fade out in the last 30 frames
        if self.timer > self.duration - 30:
            alpha = int(255 * (self.duration - self.timer) / 30)
        else:
            alpha = 255
        temp_surface = self.surface.copy()
        temp_surface.set_alpha(alpha)
        screen.blit(temp_surface, self.rect)

def create_particles(x, y, count=20):
    return [Particle(x, y) for _ in range(count)]
