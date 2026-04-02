import pygame # type: ignore
from circleshape import *
from constants import *
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y, cooldown=0):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.cooldown = cooldown
        self.velocity = pygame.Vector2(0, 0)
    
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
        self.position += self.velocity * dt

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def shoot(self):
        if self.cooldown > 0:
            return
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
        if keys[pygame.K_UP]:
            forward = pygame.Vector2(0, 1).rotate(self.rotation)
            self.velocity += forward * PLAYER_ACCELERATION * dt
        if keys[pygame.K_DOWN]:
            forward = pygame.Vector2(0, 1).rotate(self.rotation)
            self.velocity -= forward * PLAYER_ACCELERATION * dt
        if keys[pygame.K_SPACE]:
            self.shoot()

        if self.velocity.length() > PLAYER_SPEED:
            self.velocity.scale_to_length(PLAYER_SPEED)

        if self.position.x < 0:
            self.position.x += SCREEN_WIDTH
        elif self.position.x > SCREEN_WIDTH:
            self.position.x -= SCREEN_WIDTH
        if self.position.y < 0:
            self.position.y += SCREEN_HEIGHT
        elif self.position.y > SCREEN_HEIGHT:
            self.position.y -= SCREEN_HEIGHT
        
        
        self.move(dt)
        self.velocity *= DRAG

    