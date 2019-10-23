import sys, pygame
import threading, time
from gameModules import InputHandler

from how_to_draw_class import drawClass
    
def Main(): 
    game_running = True

    clock = pygame.time.Clock()
    test_draw_object = drawClass()

    while game_running:
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        test_draw_object.draw_rectangle(screen)

        # displays what we drawn.
        pygame.display.flip()
    
    pygame.quit()

if __name__ == '__main__':

    screen_size = screen_width, screen_height = 1024, 864
    black = 0,0,0
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption("Syntronic Pygame")
    pygame.init()
    Main()

