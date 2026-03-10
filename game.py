import pygame 
import math

width = 800
height = 600

class Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.tick.Clock()

        self.car_position = [400, 500]
        self.angle = 0
        self.speed = 4        

        self.reset()

    def reset(self):
        self.car_position = [400, 500]
        return self.get_state()
    
    def car_update(self, action):
        if action == 0:
            self.angle -= 0.1
        elif action == 2:
            self.angle += 0.1

        self.car_position[0] += math.cos(self.angle) * self.speed
        self.car_position[1] += math.sin(self.angle) * self.speed

    def get_state(self):
        return [
            self.car_position[0] / width,
            self.car_position[1] / height,
            math.cos(self.angle),
            math.sin(self.angle),
            self.speed / 10
        ]
    

