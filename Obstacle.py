import sys, pygame
import numpy as np
import math
import random


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
        self.vx, self.vy = 0, 0
        #self.direction = Velocity()
        self.object = pygame.image.load("Sprites/obsticle.png")

    def update(self, keys, screen_width, screen_height):
        self.x += self.vx
        self.y += self.vy

    def draw_rectangle(self,screen):
        rectangle = (self.x, self.y, self.width, self.height)
        screen.blit(self.object, (self.x, self.y))
