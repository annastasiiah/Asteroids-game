import pygame
import sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from asteroid import Asteroid
from logger import log_event

def main():
    pygame.init()

    clock = pygame.time.Clock()
    dt = 0.0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)

    AsteroidField.containers = updatable

    asteroid_field = AsteroidField()

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        dt = clock.tick(60) / 1000

        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

        screen.fill("black")

        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip()
        


if __name__ == "__main__":
    main()
