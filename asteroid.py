import pygame
import random
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x,y,radius):
      super().__init__(x, y, radius)  # Call the parent class's __init__

    def draw(self, screen):
        pygame.draw.circle(screen, "yellow", self.position, self.radius, LINE_WIDTH)
    def update(self, dt):
      self.position += (self.velocity * dt)
    #Make asteroids split or explode
    def split(self):
      self.kill()

      if self.radius <= ASTEROID_MIN_RADIUS:
        return

      log_event("asteroid_split")

      direction = random.uniform(20,50)
      velocity1 = self.velocity.rotate(direction)
      velocity2 = self.velocity.rotate(-direction)

      new_radius = self.radius - ASTEROID_MIN_RADIUS

      asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
      asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)

      asteroid1.velocity = velocity1 * 1.2
      asteroid2.velocity = velocity2 * 1.2
