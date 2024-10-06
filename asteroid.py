import random

import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, delta_time):
        self.position += (self.velocity * delta_time)

    def hit(self):
        self.kill()

        if self.radius < ASTEROID_MIN_RADIUS:
            return

        x, y = self.position
        random_angle = random.uniform(20.0, 50.0)
        rotation1 = self.velocity.rotate(random_angle)
        rotation2 = self.velocity.rotate(-random_angle)

        new_asteroid = Asteroid(x, y, self.radius - ASTEROID_MIN_RADIUS)
        new_asteroid.velocity = rotation1 * 1.2

        new_asteroid2 = Asteroid(x, y, self.radius - ASTEROID_MIN_RADIUS)
        new_asteroid2.velocity = rotation2 * 1.2
