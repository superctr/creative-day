import sys, pygame
import threading, time
from gameModules import InputHandler
def Main():

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        # displays what we drawn.
        pygame.display.flip()
    pygame.quit()

if __name__ == '__main__':

    screen_size = screen_width, screen_height = 1024, 864
    black = 0,0,0
    screen = pygame.display.set_mode(screen_size)
    pygame.init()
    Main()
