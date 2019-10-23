import sys, pygame
import NiraCar
pygame.init()

if __name__ == '__main__':

    screen_size = screen_width, screen_height = 1024, 864
    black = 0,0,0
    screen = pygame.display.set_mode(screen_size)
    screen.fill(black)
    nira_car = NiraCar.NiraCar(500,500,1024,864)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        screen.fill((0,0,0))

        nira_car.UpdatePlayer()
        nira_car.UpdateObject()
        nira_car.Draw(screen)

        # displays what we drawn.
        pygame.display.flip()
