import pygame
import circleshape
from constants import *
import random


class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position = self.position + (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20.0, 50.0)
        angle_1 = self.velocity.rotate(random_angle)
        angle_2 = self.velocity.rotate(-random_angle)
        new_size = self.radius - ASTEROID_MIN_RADIUS
        asteroid_1 = Asteroid(self.position.x, self.position.y, new_size)
        asteroid_2 = Asteroid(self.position.x, self.position.y, new_size)
        asteroid_1.velocity = angle_1 * 1.2
        asteroid_2.velocity = angle_2 * 1.2
