import pygame # type: ignore
from circleshape import *
from constants import *
from logger import log_event
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen, color="white", line_width=LINE_WIDTH):
        center = (int(self.position.x), int(self.position.y))
        pygame.draw.circle(screen, color, center, self.radius, line_width)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            random_angle = random.uniform(20, 50) 
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid1.velocity = self.velocity.rotate(random_angle)
            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid2.velocity = self.velocity.rotate(-random_angle)

