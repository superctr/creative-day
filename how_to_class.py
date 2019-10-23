import sys, pygame, math

class drawClass():
    def __init__(self):
        self.object = pygame.image.load("Sprites/Veoneer_Car.png").convert_alpha()
        self.object = pygame.transform.scale(self.object,(100,50))
        self.x, self.y = 100, 100
        self.center_x, self.center_y = 100, 100
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
        elif keys[pygame.K_DOWN] and self.speed > -20:
            self.speed -= 1

        self.speed = self.speed * 0.95

        radians = self.angle * math.pi / 180.
        self.x += math.cos(radians) * self.speed
        self.y += math.sin(radians) * self.speed
        self.center_x = int(self.x + self.height / 2)
        self.center_y = int(self.y + self.width / 2)

    def draw_rectangle(self,screen):

        #rectangle = (self.x, self.y, self.width, self.height)
        #pygame.draw.rect(screen, self.color, rectangle)
        center = self.object.get_rect().center
        rotated_image = pygame.transform.rotate(self.object, -self.angle)
        new_rect = rotated_image.get_rect(center = center)
        new_rect.x += self.x
        new_rect.y += self.y
        screen.blit(rotated_image, new_rect.topleft)
        pygame.draw.circle(screen, (255,0,0), (self.center_x, self.center_y), 5)
