import pygame, sys
from constants import *
from logger import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *  
from points import *
from lives import *

def main():
    pygame.init()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)
    asteroid_field = AsteroidField()
    clock = pygame.time.Clock()
    dt = 0
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Asteroids')
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    points, text, textRect = start_points()
    lives, lives_text, livesRect = start_lives()

    floating_texts = []
    player_lives = PLAYER_LIVES
 
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        screen.blit(text, textRect)
        screen.blit(lives_text, livesRect)
        updatable.update(dt)
 
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                player_lives -= 1
                if  player_lives <= 0:
                    print("Player hit an asteroid! Game over!")
                    sys.exit()
                print("Player hit an asteroid! Lives remaining:", player_lives)
                log_event("player_hit")
                lives, lives_text, livesRect = update_lives(lives)
                for asteroid in asteroids:
                    asteroid.kill()
                player.position = pygame.Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
                break
 
        for shot in shots:
            for asteroid in asteroids:
                if shot.collides_with(asteroid):
                    log_event("asteroid_shot")
                    shot.kill()
                    asteroid.split()
                    points, text, textRect = update_points(points)
                    floating_texts.append(asteroid_point(asteroid))
 
        for obj in drawable:
            obj.draw(screen)
 
        # Update and draw all floating +10 texts
        for ft in floating_texts:
            ft.update()
            ft.draw(screen)
        floating_texts = [ft for ft in floating_texts if ft.alive]
 
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        
if __name__ == "__main__":
    main()