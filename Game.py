import sys, pygame
import threading, time
import random
from how_to_class import drawClass
from Obstacle import obsticleClass

def CheckColision(player_list, obstacle_list):
    for player in player_list:
        for obstacle in obstacle_list:
            if (abs(player.center_x - obstacle.center_x) < (player.width / 2) and abs(player.center_y - obstacle.center_y) < (player.width / 2)):
                #Colision reached
                obstacle_list.pop(obstacle_list.index(obstacle))

def Main(): 
    game_running = True
    clock = pygame.time.Clock()
    
    player_list = []
    obstacle_list = []

    test_draw_object = drawClass(screen_width, screen_height)

    player_list.append(test_draw_object)

    while game_running:
        clock.tick(30)

        screen.blit(parking_bg, (0,0))
        keys = pygame.key.get_pressed()

        random_number = random.randint(0,100)
        if random_number > 97 and len(obstacle_list) < 4:
            obstacle_list.append(obsticleClass(screen_width, screen_height))
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
        for player in player_list:
            player.update(keys,screen_width, screen_height)
            player.draw(screen)
        for obstacle in obstacle_list:
            if obstacle.remove:
                obstacle_list.pop(obstacle_list.index(obstacle))
            obstacle.update(keys,screen_width, screen_height)
            obstacle.draw(screen)
        CheckColision(player_list, obstacle_list)

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

