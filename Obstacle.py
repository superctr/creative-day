import sys, pygame
import numpy as np
import math
import random

class obsticleClass():
    def __init__(self,screen_width, screen_height):
        self.x, self.y = 100, 100
        self.width = 100
        self.height = 100
        self.color = (0,255,0)

        self.vx, self.vy = random.randint(-10,10), random.randint(-10,10)
        if abs(self.vx)>abs(self.vy):
            self.y = random.randint(0,screen_width)
            if self.vx>0:
                self.x = 0
            else:
                self.x = screen_width
        else:
            self.x = random.randint(0,screen_height)
            if self.vy>0:
                self.y = 0
            else:
                self.y = screen_height


        self.object = pygame.image.load("Sprites/obsticle3.png")
        self.object = pygame.transform.scale(self.object,(self.width,self.height))

    def update(self, keys, screen_width, screen_height):
        self.x += self.vx
        self.y += self.vy

    def draw_rectangle(self,screen):
        rectangle = (self.x, self.y, self.width, self.height)
        screen.blit(self.object, (self.x, self.y))
