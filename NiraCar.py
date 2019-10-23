import sys, pygame

class NiraCar:
    def __init__(self,x,y,screen_x,screen_y):
        self.object = pygame.image.load("Sprites/Nira_Car.png")
        self.x = x
        self.y = y
        self.screen_x = screen_x
        self.screen_y = screen_y

    def UpdatePlayer(self):
        pass

    def UpdateObject(self):
        pass

    def Draw(self, screen):
        screen.blit(self.object, (self.x, self.y))
