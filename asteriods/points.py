import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT


class FloatingText:
    def __init__(self, text, x, y, duration=90):  # ~1.5s at 60fps
        self.x = x
        self.y = y
        self.duration = duration
        self.timer = 0
        self.alive = True

        green = (0, 255, 0)
        font = pygame.font.Font('freesansbold.ttf', 32)
        self.surface = font.render(text, True, green)
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
    green = (0, 255, 0)
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render((Points_text + points), True, green)
    textRect = text.get_rect()
    textRect.center = (100, 50)
    return points, text, textRect


def update_points(points):
    Points_text = "Points: "
    points = str(int(points) + 10)
    green = (0, 255, 0)
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render((Points_text + points), True, green)
    textRect = text.get_rect()
    textRect.center = (100, 50)
    return points, text, textRect


def asteroid_point(asteroid):
    return FloatingText("+10", asteroid.position.x, asteroid.position.y, duration=30)