import sys, pygame
import threading, time
import random
from how_to_class import drawClass
from Obstacle import obsticleClass
from Veoneer_Car_Class import drawVeoneerClass

def CheckColision(player_list, obstacle_list, bullet_list):
    for obstacle in obstacle_list:
        obstacle_hit = False
        for player in player_list:
            if (abs(player.center_x - obstacle.center_x) < (player.width / 2) and abs(player.center_y - obstacle.center_y) < (player.width / 2)):
                #Colision reached, destroy car and obstacle
                player_list.pop(player_list.index(player))
                obstacle_hit = True
        if(obstacle_hit):
                obstacle_list.pop(obstacle_list.index(obstacle))
    for bullet in bullet_list:
        bullet_hit = 0
        for obstacle in obstacle_list:
            if (abs(bullet.center_x - obstacle.center_x) < (obstacle.width) and abs(bullet.center_y - obstacle.center_y) < (obstacle.width)):
                obstacle_list.pop(obstacle_list.index(obstacle))
                bullet_hit = bullet_hit + 1
                score[bullet.creator] = score[bullet.creator] + (10 * bullet_hit)
        if(bullet_hit):
                bullet_list.pop(bullet_list.index(bullet))


def Main(): 
    game_running = True
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("monospace", 16)
    
    score[0] = 0
    score[1] = 0
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

        # check if all players are dead
        if len(player_list) == 0:
            return

        random_number = random.randint(0,100)
        if random_number > 90 and len(obstacle_list) < 8:
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
        scoretext = font.render("Player 1: %d" % (score[0]), 1, (255,255,255))
        screen.blit(scoretext,(5,5))
        scoretext = font.render("Player 2: %d" % (score[1]), 1, (255,255,255))
        screen.blit(scoretext,(805,5))

        pygame.display.flip()

def GameOver():
    game_running = True
    clock = pygame.time.Clock()
    bigfont = pygame.font.SysFont("monospace", 50)
    font = pygame.font.SysFont("monospace", 16)
    while game_running:
        clock.tick(30)
        screen.set_alpha(5)
        screen.fill((5,5,5),None,pygame.BLEND_SUB)
        screen.set_alpha(255)
        keys = pygame.key.get_pressed()
        scoretext = bigfont.render("GAME OVER", 1, (255,255,255))
        screen.blit(scoretext,(500,300))
        scoretext = font.render("Press enter to restart", 1, (255,255,255))
        screen.blit(scoretext,(500,400))
        scoretext = font.render("Player 1: %d" % (score[0]), 1, (255,255,255))
        screen.blit(scoretext,(5,5))
        scoretext = font.render("Player 2: %d" % (score[1]), 1, (255,255,255))
        screen.blit(scoretext,(805,5))
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if keys[pygame.K_RETURN]:
                return 0
        pygame.display.flip()
    return 1

if __name__ == '__main__':
    score = [0,0]
    screen_size = screen_width, screen_height = 1200, 900
    black = 0,0,0
    screen = pygame.display.set_mode(screen_size)
    parking_bg = pygame.image.load('parking.jpg')
    parking_bg = pygame.transform.scale(parking_bg,(screen_width,screen_height))
    pygame.display.set_caption("Syntronic Pygame")
    pygame.init()
    while(1):
        Main()
        if GameOver():
            break
    pygame.quit()

