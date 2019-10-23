import sys, pygame
import threading, time
import random
from how_to_class import drawClass
from Obstacle import obsticleClass
from Veoneer_Car_Class import drawVeoneerClass

def CheckColision(player_list, obstacle_list, bullet_list):
    player_number = 0
    for player in player_list:
        for obstacle in obstacle_list:
            if (abs(player.center_x - obstacle.center_x) < (player.width / 2) and abs(player.center_y - obstacle.center_y) < (player.width / 2)):
                #Colision reached, destroy car and obstacle
                player_list.pop(player_list.index(player))
                obstacle_list.pop(obstacle_list.index(obstacle))
    for bullet in bullet_list:
        for obstacle in obstacle_list:
            if (abs(bullet.center_x - obstacle.center_x) < (obstacle.width) and abs(bullet.center_y - obstacle.center_y) < (obstacle.width)):
                bullet_list.pop(bullet_list.index(bullet))
                obstacle_list.pop(obstacle_list.index(obstacle))
        player_number = player_number + 1

def Main(): 
    game_running = True
    clock = pygame.time.Clock()
    
    player_list = []
    obstacle_list = []
    bullet_list = []

    test_draw_object = drawClass(screen_width, screen_height)
    test_draw_object2 = drawVeoneerClass(screen_width, screen_height)

    player_list.append(test_draw_object)
    player_list.append(test_draw_object2)

    while game_running:
        clock.tick(30)

        screen.blit(parking_bg, (0,0))
        keys = pygame.key.get_pressed()

        random_number = random.randint(0,100)
        if random_number > 90 and len(obstacle_list) < 12:
            obstacle_list.append(obsticleClass(screen_width, screen_height))
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
        for player in player_list:
            player.update(keys,screen_width, screen_height, bullet_list)
            player.draw(screen)
        for obstacle in obstacle_list:
            if obstacle.remove:
                obstacle_list.pop(obstacle_list.index(obstacle))
            obstacle.update(keys,screen_width, screen_height)
            obstacle.draw(screen)
        for bullet in bullet_list:
            if bullet.remove:
                bullet_list.pop(bullet_list.index(bullet))
            bullet.update(keys,screen_width, screen_height)
            bullet.draw(screen)
        CheckColision(player_list, obstacle_list, bullet_list)

        pygame.display.flip()
    
    pygame.quit()

if __name__ == '__main__':

    screen_size = screen_width, screen_height = 1200, 900
    black = 0,0,0
    screen = pygame.display.set_mode(screen_size)
    parking_bg = pygame.image.load('parking.jpg')
    parking_bg = pygame.transform.scale(parking_bg,(screen_width,screen_height))
    pygame.display.set_caption("Syntronic Pygame")
    pygame.init()
    Main()

