import sys,pygame,math
class bullet():
    def __init__(self,screen_width,screen_height,x,y,angle,creator):
        self.x = x
        self.y = y
        self.angle = angle
        self.width = 5
        self.height = 5
        self.center_x, self.center_y = self.x + self.width/2, self.y + self.height/2
        self.speed = 30
        self.creator = creator
        self.remove = False

    def update(self, keys, screen_width, screen_height):
        radians = self.angle * math.pi / 180.
		
        self.delta_x = math.cos(radians) * self.speed
        self.delta_y = math.sin(radians) * self.speed

        self.x += self.delta_x
        self.y += self.delta_y
        self.center_x = int(self.x + self.width / 2)
        self.center_y = int(self.y + self.height / 2)

        # wall collision x
        if(self.center_x < 0 or self.center_x > screen_width or
           self.center_y < 0 or self.center_y > screen_height):
           self.remove = True


    def draw(self,screen):
        pygame.draw.circle(screen, (255,0,0), (self.center_x, self.center_y), 5)

