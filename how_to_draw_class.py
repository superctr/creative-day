import sys, pygame

class drawClass():
    def __init__(self):
        self.x, self.y = 100, 100
        self.width = 50
        self.height = 100
        self.color = (0,255,0)

    def draw_rectangle(self,screen):
        rectangle = (self.x, self.y, self.width, self.height)
        pygame.draw.rect(screen, self.color, rectangle)
