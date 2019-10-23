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
   
    def draw_rectangle(self, screen):
        rectangle = (self.x, self.y, self.width, self.height)
        pygame.draw.rect(screen, self.color, rectangle)
    
    def set_color(r,g,b)
        self.color = (r, g, b)

    def set_damage(self, damage)
        self.damage = damage

    def get_damage()
        return(self.damage)

    def set_name(self,name)
        self.name = name 

    def get_name()
        return(self.name)

    def set_speed(self, speed)
        self.speed = speed

    def get_speed()
        return(self.speed)

    def set_status(self, status)
        if status = True:
            self.remove = True
        else:
            self.remove = False

    def get_status()
        return(self.remove)

    def set_sprite(self, sprite)
        self.sprite =  pygame.image.load(sprite)

    def get_sprite()
        return(self.sprite)

    

    