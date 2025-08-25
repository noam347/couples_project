import time

import pygame
import consts
import random
grass = pygame.image.load(consts.GRASS_IMG)
soldier = pygame.image.load(consts.SOLDIER_NIGTH_IMG)
nigth_soldier = pygame.image.load(consts.SOLDIER_NIGTH_IMG)
mine = pygame.image.load(consts.MINE_IMG)
tile_size = consts.WINDOW_HEIGHT//consts.GRID_ROWS

def randomize_grass_location():
    x_location = random.randrange(0, consts.WINDOW_WIDTH-60)
    y_location = random.randrange(0, consts.WINDOW_HEIGHT-60)
    return  x_location,y_location


def add_grass(screen):
    for i in range(20):
        screen.blit(grass, (randomize_grass_location()))

def create_regular_screen():
    pygame.init()
    screen = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
    pygame.display.set_caption('The flag')
    screen.fill(consts.BACKGROUND_COLOR)
    add_grass(screen)
    pygame.display.flip()
    return screen

def create_x_ray_board(real_matrix,soldier_location):
    x_ray_screen = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
    pygame.display.set_caption('The flag')
    x_ray_screen.fill(consts.X_RAY_BACKGROUND)
    for y in range(0, consts.GRID_ROWS * 20, tile_size):
        pygame.draw.lines(x_ray_screen, consts.X_RAY_LINES, True, ((0, y), (consts.WINDOW_WIDTH, y)))

    for x in range(0, consts.GRID_COLUMNS * 20, tile_size):
        pygame.draw.lines(x_ray_screen,consts.X_RAY_LINES, True, ((x, 0), (x, consts.WINDOW_HEIGHT)))

    x_ray_screen.blit(nigth_soldier,soldier_location)

    for row in range(len(real_matrix)):
        for col in range(len(real_matrix[row])-2):
            if real_matrix[row][col] == "mine" and real_matrix[row][col+1] == "mine" and real_matrix[row][col+2] == "mine" :
                x_ray_screen.blit(mine,(col*tile_size,row*tile_size))
    pygame.display.flip()


def updated_location(screen,soldier_location):
    screen.blit(soldier, soldier_location)
    time.sleep(1)






updated_location(create_regular_screen(),[0,0])
# grass_height = consts.WINDOW_HEIGHT//consts.GRID_COLUMNS
# print(grass_height)
# grass_width = consts.WINDOW_WIDTH//consts.GRID_ROWS
# print(grass_width)
# # pygame.transform.scale(grass,(grass_width,grass_height))
# pygame.transform.scale(grass,(750,500))



