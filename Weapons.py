import sys, pygame

class WeaponsClass():
    def __init__(self, x, y, width, height):
        self.x, self.y = x, y
        self.width = width
        self.height = height
        self.speed = 0
        self.direction = 0
        self.color = (0, 150, 0)
        self.damage = 0
        self.name = ""
        self.remove = False
        self.sprite = ""
        self.sprite 
        self.explosion = False
        self.explosion_sprite = False
        self.display = False
        self.angle = 0
   
    def draw_weapon(self, screen):
        center = self.object.get_rect().center
        rotated_image = pygame.transform.rotate(self.object, -self.angle)
        new_weapon = rotated_image.get_rect(center = center)
        new_weapon.x += self.x
        new_weapon.y += self.y 
        screen.blit(rotated_image, new_rect.topleft)
        pygame.draw.circle(screen, (255,0,0), (self.center_x, self.center_y), 5)
    
    def update(self, screen_width, screen_height, speed_x, speed_y):
            self.x =+ speed_x
            self.y =+ speed_y

    def set_damage(self, damage):
        self.damage = damage
        
    def set_name(self,name):
        self.name = name 

    def set_status(self, status):
        if status == True:
            self.remove = True
        else:
            self.remove = False

    def set_speed(self, speed):
        self.speed = speed

    def set_sprite(self, sprite):
        self.sprite =  pygame.image.load(sprite).convert_alpha()

    def set_explosion(self, status):
        if status == True:
            self.explosion = True
        else:
            self.explosion = False

    def set_explosion_sprite(self, sprite):
        self.explosion_sprite = pygame.image.load(sprite).convert_alpha()
        
    def get_damage(self):
        return(self.damage)

    def get_name(self):
        return(self.name)

    def get_speed(self):
        return(self.speed)

    def get_status(self):
        return(self.remove)
    
    def get_sprite(self):
        return(self.sprite)

    def get_explosion(self):
        return(self.explosion)

    def get_explosion_sprite(self):
        return(self.explosion_sprite)


def Make_Bullet (x, y, speed_x, speed_y):
    Bullet = WeaponsClass(x,y, width, height)
    Bullet.set_sprite('.../Sprites/bullet.png')
    Bullet.set_speed(10)
    Bullet.set_damage(10)




    

    

    