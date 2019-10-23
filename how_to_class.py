import sys, pygame, math

class drawClass():
    def __init__(self):
        self.x, self.y = 100, 100
        self.width = 50
        self.height = 100
        self.color = (0,255,0)
        self.speed = 1
        self.angle = 0

    def update(self, keys, screen_width, screen_height):
        if keys[pygame.K_LEFT]:
            self.angle -= 5
        elif keys[pygame.K_RIGHT]:
            self.angle += 5
        self.angle = self.angle % 360

        if keys[pygame.K_UP] and self.speed < 20:
            self.speed += 1
        elif keys[pygame.K_DOWN] and self.speed > 0:
            self.speed -= 1

        radians = self.angle * math.pi / 180.
        self.x += math.cos(radians) * self.speed
        self.y += math.sin(radians) * self.speed

    def draw_rectangle(self,screen):
        rectangle = (self.x, self.y, self.width, self.height)
        pygame.draw.rect(screen, self.color, rectangle)
