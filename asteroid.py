from circleshape import *
from constants import *
from random import uniform

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)


    def draw(self, screen):
        pygame.draw.circle(screen,
                           "orange",
                           self.position,
                           self.radius,
                           2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = uniform(20, 50)
        new_angle_1 = self.velocity.rotate(angle)
        new_angle_2 = self.velocity.rotate(angle * -1)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid_1 = Asteroid(*(self.position), new_radius)
        asteroid_2 = Asteroid(*(self.position), new_radius)
        asteroid_1.velocity = new_angle_1 * 1.2
        asteroid_2.velocity = new_angle_2 * 1.2
