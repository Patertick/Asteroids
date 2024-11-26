import pygame
import random

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):

    containers = []

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)
    def update(self, dt):
        self.position += self.velocity * dt
    def split(self):
        self.kill()
        if(self.radius <= ASTEROID_MIN_RADIUS):
            return
        angle = random.uniform(20, 50)
        direction_first = self.velocity.rotate(angle)
        direction_second = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid_first = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_second = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_first.velocity = direction_first * 1.2
        asteroid_second.velocity = direction_second * 1.2