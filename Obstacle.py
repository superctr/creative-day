import sys, pygame
import numpy as np
import math

OBSTACLE_SPEED_VEC = velocity()

class velocity():
    def __init__(self, x, y):
        speed, direction = self.normalizeVector(x, y)
        self.speed = speed
        self.direction = direction

    def normalizeVector(self, x, y):
        speed = math.sqrt(math.pow(x,2) + math.pow(y,2))
        newV = [x/speed, y/speed]
        return speed, newV

class obsticleClass():
    def __init__(self):
        self.x, self.y = 100, 100
        self.width = 50
        self.height = 100
        self.color = (0,255,0)
        self.speed = 20
        self.direction = Velocity()

    def update(self, keys, screen_width, screen_height):
        if keys[pygame.K_LEFT] and self.x > (0):
            self.x -= self.speed
        elif keys[pygame.K_RIGHT] and self.x < (screen_width - self.width):
            self.x += self.speed
        elif keys[pygame.K_UP] and self.y > (0):
            self.y -= self.speed
        elif keys[pygame.K_DOWN] and self.y < (screen_height - self.height):
            self.y += self.speed
            elif keys[pygame.K_DOWN] and self.y < (screen_height - self.height):
            self.y += self.speed

    def draw_rectangle(self,screen):
        rectangle = (self.x, self.y, self.width, self.height)
        pygame.draw.rect(screen, self.color, rectangle)
