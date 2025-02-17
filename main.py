import sys
import pygame
from constants import (SCREEN_WIDTH, SCREEN_HEIGHT)
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from bullet import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    asteroids = pygame.sprite.Group()
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = updateable
    Shot.containers = (shots, updateable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updateable.update(dt)

        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collisions(shot):
                    shot.kill()
                    asteroid.split()
            if asteroid.collisions(player):
                print("Game Over!")
                sys.exit()

        screen.fill("black")
        for item in drawable:
            item.draw(screen)
        pygame.display.flip()

        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
