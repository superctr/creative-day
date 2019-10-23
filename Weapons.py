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
        self.explosion = False
        self.explosion_sprite = False
   
    def draw_rectangle(self, screen):
        rectangle = (self.x, self.y, self.width, self.height)
        pygame.draw.rect(screen, self.color, rectangle)
    
    def set_color(self, r, g, b):
        self.color = (r, g, b)

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


def Make_Bullet (x, y, width, height, direction, Nbr):
    Bullet = WeaponsClass(x,y, width, height)
    Bullet.set_name = "Bullet" + str(Nbr)
    Bullet.set_sprite('.../Sprites/bullet.png')
    Bullet.set_speed(10)



    

    

    