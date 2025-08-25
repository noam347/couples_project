import pygame
import consts
import random
grass = pygame.image.load(consts.GRASS_IMG)
soldier = pygame.image.load(consts.SOLDIER_IMG)
flag = pygame.image.load(consts.FLAG_IMG)
nigth_soldier = pygame.image.load(consts.SOLDIER_NIGTH_IMG)
mine = pygame.image.load(consts.MINE_IMG)
tile_size = consts.WINDOW_HEIGHT//consts.GRID_ROWS

def randomize_grass_location():
    grass_location = []
    for i in range(20):
        x_location = random.randrange(0, consts.WINDOW_WIDTH-60)
        y_location = random.randrange(0, consts.WINDOW_HEIGHT-60)
        location = (x_location,y_location)
        grass_location.append(location)
    return  grass_location


def add_grass(screen,grass_locations):
    for location in grass_locations:
        screen.blit(grass,location)


def create_regular_screen(grass_locations):
    pygame.init()
    screen = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
    pygame.display.set_caption('The flag')
    screen.fill(consts.BACKGROUND_COLOR)
    for location in grass_locations:
        screen.blit(grass, location)
    screen.blit(flag,(46*20,21*20))
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
    pygame.display.flip()


def draw_lose_message(game_screen):
    draw_message(game_screen,consts.LOSE_MESSAGE, consts.LOSE_FONT_SIZE,
                 consts.LOSE_COLOR, consts.LOSE_LOCATION)
    pygame.display.flip()


def draw_win_message(game_screen):
    draw_message(game_screen, consts.WIN_MESSAGE, consts.WIN_FONT_SIZE,
                 consts.WIN_COLOR, consts.WIN_LOCATION)
    pygame.display.flip()

def draw_start_message(game_screen):
    draw_message(game_screen, consts.START_MESSAGE, consts.START_FONT_SIZE,
                 consts.START_COLOR, consts.START_LOCATION)
    pygame.display.flip()


def draw_message(screen,message, font_size, color, location):
    font = pygame.font.SysFont(consts.FONT_NAME, font_size)
    text_img = font.render(message, True, color)
    screen.blit(text_img, location)



