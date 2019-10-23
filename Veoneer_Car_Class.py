import sys, pygame, math
import Weapons 

class drawVeoneerClass():
    def __init__(self):
        self.x, self.y = 200, 200
        self.center_x, self.center_y = 100, 100
        self.delta_x, self.delta_y = 0, 0
        self.width = 100
        self.height = 50
        self.object = pygame.image.load("Sprites/Veoneer_Car.png").convert_alpha()
        self.object = pygame.transform.scale(self.object,(self.width,self.height))
        self.color = (0,255,0)
        self.speed = 1
        self.angle = 0
        self.shoot = 0
		
    def update(self, keys, screen_width, screen_height):
        if keys[pygame.K_a]:
            self.angle -= 5
        elif keys[pygame.K_d]:
            self.angle += 5
        self.angle = self.angle % 360

        if keys[pygame.K_w] and self.speed < 20:
            self.speed += 1
        elif keys[pygame.K_s] and self.speed > -20:
            self.speed -= 1
		
        if keys[pygame.K_SPACE]:
            print("Hi")
            self.shoot = 1
            #Weapons.Make_Bullet(self.center_x+50, self.center_y+50, screen )
        self.speed = self.speed * 0.95
        radians = self.angle * math.pi / 180.

        self.delta_x = math.cos(radians) * self.speed
        self.delta_y = math.sin(radians) * self.speed
        # wall collision x
        if(self.center_x + self.delta_x < 5 or self.center_x + self.delta_x > 1019 or
           self.center_y + self.delta_y < 5 or self.center_y + self.delta_y > 859):
            self.speed = self.speed * -0.1
            self.delta_x = math.cos(radians) * self.speed
            self.delta_y = math.sin(radians) * self.speed

        self.x += self.delta_x
        self.y += self.delta_y
		
        self.center_x = int(self.x + self.width / 2)
        self.center_y = int(self.y + self.height / 2)
    def draw(self,screen):
        if self.angle:
            Weapons.Make_Bullet(self.center_x+50, self.center_y+50,10,10, screen )    
		#rectangle = (self.x, self.y, self.width, self.height)
        #pygame.draw.rect(screen, self.color, rectangle)
        center = self.object.get_rect().center
        rotated_image = pygame.transform.rotate(self.object, -self.angle)
        new_rect = rotated_image.get_rect(center = center)
        new_rect.x += self.x
        new_rect.y += self.y
        screen.blit(rotated_image, new_rect.topleft)
        pygame.draw.circle(screen, (255,0,0), (self.center_x, self.center_y), 5)
