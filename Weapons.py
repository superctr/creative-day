import sys, pygame 

class WeaponsClass():
    def __init__(self, x, y, width, height):
        self.x, self.y = x, y
        self.width = width
        self.height = height
        self.color = (0, 150, 0)

    def draw_rectangle(self, screen):
        rectangle = (self.x, self.y, self.width, self.height)
        pygame.draw.rect(screen, self.color, rectangle)