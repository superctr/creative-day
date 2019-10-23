import sys, pygame
import math
import random

OBSTACLE_SPEED_CONST = 6

class obsticleClass():
    def __init__(self,screen_width, screen_height):
        self.x, self.y = 100, 100
        self.creator = -1
        self.width = 65
        self.height = 65
        self.center_x, self.center_y = self.x + self.width/2, self.y + self.height/2
        self.color = (0,255,0)
        self.vx, self.vy = random.randint(-10,10), random.randint(-10,10)
        if self.vx == 0 and self.vy == 0:
            self.vx = 1
            self.vy = 0
        self.normalizeSpeed()
        self.SetInitialPosition(screen_width, screen_height)
        self.object = pygame.image.load("Sprites/obsticle3.png")
        self.object = pygame.transform.scale(self.object,(self.width,self.height))
        self.remove = False

    def SetInitialPosition(self,screen_width, screen_height):
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

    def normalizeSpeed(self):
        norm = math.sqrt(math.pow(self.vx,2) + math.pow(self.vy,2))
        self.vx = self.vx * OBSTACLE_SPEED_CONST / norm
        self.vy = self.vy * OBSTACLE_SPEED_CONST / norm

    def update(self, keys, screen_width, screen_height):
        self.x += self.vx
        self.y += self.vy
        self.center_x, self.center_y = self.x + self.width/2, self.y +  self.height/2
        if self.x < 0 or self.x > screen_width or self.y < 0 or self.y > screen_height:
            self.remove = True

    def draw(self,screen):
        rectangle = (self.x, self.y, self.width, self.height)
        screen.blit(self.object, (self.x, self.y))
        #Red dot on Obstacle
        #pygame.draw.circle(screen, (255,0,0), (int(self.center_x), int(self.center_y)), 5)
