from constants import *
from circleshape import *
from logger import log_state
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
         pygame.draw.circle(screen, 'white', self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            new_angle = random.uniform(20, 50)

            new_velocity = self.velocity.rotate(new_angle)

            new_velocity_2 = -(self.velocity.rotate(new_angle))

            new_radius = self.radius - ASTEROID_MIN_RADIUS

            a1 = Asteroid(self.position.x, self.position.y, new_radius)
            a2 = Asteroid(self.position.x, self.position.y, new_radius)

            a1.velocity = new_velocity * 1.2
            a2.velocity = new_velocity_2 


