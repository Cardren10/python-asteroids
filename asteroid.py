import pygame
from circleshape import CircleShape
import constants
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return
        
        angle = random.uniform(20, 50)

        dir_a = self.velocity.rotate(angle)
        dir_b = self.velocity.rotate(-angle)
        new_radius = self.radius - constants.ASTEROID_MIN_RADIUS

        ast_a = Asteroid(self.position.x, self.position.y, new_radius)
        ast_a.velocity = dir_a * 1.2
        ast_b = Asteroid(self.position.x, self.position.y, new_radius)
        ast_b.velocity = dir_b * 1.2