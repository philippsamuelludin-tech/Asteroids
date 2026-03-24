import pygame # type: ignore
from constants import * 
from circleshape import *


class Shot(CircleShape):
    def __init__(self, x, y, velocity):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = velocity

    def draw(self, screen, color="white", line_width=LINE_WIDTH):
        center = (int(self.position.x), int(self.position.y))
        pygame.draw.circle(screen, color, center, self.radius, line_width)

    def update(self, dt):
        self.position += self.velocity * dt