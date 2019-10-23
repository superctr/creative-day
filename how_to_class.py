import sys, pygame

class drawClass():
    def __init__(self):
        self.x, self.y = 100, 100
        self.width = 50
        self.height = 100
        self.color = (0,255,0)
        self.speed = 20

    def update(self, keys, screen_width, screen_height):
        if keys[pygame.K_LEFT] and self.x > (0):
            self.x -= self.speed
        elif keys[pygame.K_RIGHT] and self.x < (screen_width - self.width):
            self.x += self.speed
        elif keys[pygame.K_UP] and self.y > (0):
            self.y -= self.speed
        elif keys[pygame.K_DOWN] and self.y < (screen_height - self.height):
            self.y += self.speed 

    def draw_rectangle(self,screen):
        rectangle = (self.x, self.y, self.width, self.height)
        pygame.draw.rect(screen, self.color, rectangle)
