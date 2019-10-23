import sys, pygame, math
from bullet import bullet

class drawClass():
    def __init__(self, screen_width, screen_height):
        self.x, self.y = 200, 200
        self.screen_width = screen_width - 5
        self.screen_height = screen_height - 5
        self.width = 100
        self.height = 50
        self.center_x = int(self.x + self.width / 2)
        self.center_y = int(self.y + self.height / 2)
        self.object = pygame.image.load("Sprites/Veoneer_Car.png").convert_alpha()
        self.object = pygame.transform.scale(self.object,(self.width,self.height))
        self.delta_x, self.delta_y = 0, 0
        self.speed = 1
        self.angle = 0
        self.bullet_timeout = 0

    def update(self, keys, screen_width, screen_height, obstacle_list):
        if keys[pygame.K_LEFT]:
            self.angle -= min(abs(self.speed), 5)
        elif keys[pygame.K_RIGHT]:
            self.angle += min(abs(self.speed), 5)
        self.angle = self.angle % 360

        if keys[pygame.K_UP] and self.speed < 20:
            self.speed += 1
        elif keys[pygame.K_DOWN] and self.speed > -20:
            self.speed -= 1

        if self.bullet_timeout > 0:
            self.bullet_timeout = self.bullet_timeout - 1
        elif keys[pygame.K_SPACE]:
            # Space is held, there is an autofire limit
            obstacle_list.append(bullet(screen_width,screen_height,self.center_x,self.center_y,self.angle,0))
            self.bullet_timeout = 9
        else:
            # Space is released, we can fire immediately after.
            self.bullet_timeout = 0

        self.speed = self.speed * 0.95
        radians = self.angle * math.pi / 180.
		
        self.delta_x = math.cos(radians) * self.speed
        self.delta_y = math.sin(radians) * self.speed

        # wall collision x
        if(self.center_x + self.delta_x < 5 or self.center_x + self.delta_x > screen_width or
           self.center_y + self.delta_y < 5 or self.center_y + self.delta_y > screen_height):
            self.speed = self.speed * -0.1
            self.delta_x = math.cos(radians) * self.speed
            self.delta_y = math.sin(radians) * self.speed

        self.x += self.delta_x
        self.y += self.delta_y
        self.center_x = int(self.x + self.width / 2)
        self.center_y = int(self.y + self.height / 2)

    def draw(self,screen):
        center = self.object.get_rect().center
        rotated_image = pygame.transform.rotate(self.object, -self.angle)
        new_rect = rotated_image.get_rect(center = center)
        new_rect.x += self.x
        new_rect.y += self.y
        screen.blit(rotated_image, new_rect.topleft)
        pygame.draw.circle(screen, (255,0,0), (self.center_x, self.center_y), 5)
