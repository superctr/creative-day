import sys, pygame
import threading, time
#from gameModules import InputHandler

from how_to_class import drawClass
from Obstacle import obsticleClass
    
def Main(): 
    game_running = True

    clock = pygame.time.Clock()
    test_draw_object = drawClass()
    Test_obsticle = obsticleClass(screen_width, screen_height)

    while game_running:
        clock.tick(30)
        screen.blit(parking_bg, (0,0))

        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        test_draw_object.update(keys,screen_width, screen_height)
        test_draw_object.draw_rectangle(screen)

        Test_obsticle.draw_rectangle(screen)
        Test_obsticle.update(keys,screen_width, screen_height)

        # displays what we drawn.
        pygame.display.flip()
    
    pygame.quit()

if __name__ == '__main__':

    screen_size = screen_width, screen_height = 1024, 864
    black = 0,0,0
    screen = pygame.display.set_mode(screen_size)

    parking_bg = pygame.image.load('parking.jpg')
    pygame.display.set_caption("Syntronic Pygame")
    pygame.init()
    Main()

