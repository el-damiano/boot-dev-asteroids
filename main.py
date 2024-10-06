import sys
import pygame
from constants import *
from asteroidfield import AsteroidField
from asteroid import Asteroid
from player import Player
from bullet import Bullet


def main():
    print(f"""Starting asteroids!
Screen width: {SCREEN_WIDTH}
Screen height: {SCREEN_HEIGHT}""")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    delta_time = 0

    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    bullets = pygame.sprite.Group()

    AsteroidField.containers = (updatables)
    asteroid_field = AsteroidField()

    Asteroid.containers = (asteroids, updatables, drawables)

    Player.containers = (updatables, drawables)
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)

    Bullet.containers = (updatables, drawables, bullets)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatables.update(delta_time)

        for asteroid in asteroids:
            if asteroid.is_colliding(player):
                print('Game Over!')
                sys.exit()

            for bullet in bullets:
                if asteroid.is_colliding(bullet):
                    asteroid.hit()
                    bullet.kill()

        screen.fill("black")

        for sprite in drawables:
            sprite.draw(screen)

        pygame.display.flip()

        delta_time = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
