import pygame # type: ignore
from circleshape import *
from constants import *
from main import main
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y, cooldown=0):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.cooldown = cooldown
    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)

    def move(self, dt):
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def shoot(self):
        if self.cooldown > 0:
            return
        else:
            self.cooldown = PLAYER_SHOOT_COOLDOWN_SECONDS
            shot_velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
            Shot(self.position.x, self.position.y, shot_velocity)


    def update(self, dt):
        self.cooldown -= dt
        keys = pygame.key.get_pressed()


        if keys[pygame.K_LEFT]:
            self.rotate(-dt)
        if keys[pygame.K_RIGHT]:
            self.rotate(dt)
        if keys[pygame.K_DOWN]:
            self.move(-dt)
        if keys[pygame.K_UP]:
            self.move(dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

    