import pygame
import consts
import random




pygame.init()
screen = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
pygame.display.set_caption('The flag')
screen.fill(consts.BACKGROUND_COLOR)
pygame.display.flip()
    # return screen



grass = pygame.image.load(consts.GRASS_IMG)
# grass_height = consts.WINDOW_HEIGHT//consts.GRID_COLUMNS
# print(grass_height)
# grass_width = consts.WINDOW_WIDTH//consts.GRID_ROWS
# print(grass_width)
# # pygame.transform.scale(grass,(grass_width,grass_height))
# pygame.transform.scale(grass,(750,500))


def randomize_grass_location():
    x_location = random.randrange(0, consts.WINDOW_WIDTH-60)
    y_location = random.randrange(0, consts.WINDOW_HEIGHT-60)
    return  x_location,y_location


def add_grass():
    for i in range(20):
        screen.blit(grass, (randomize_grass_location()))

add_grass()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()




BG = (4, 10, 2)
GREEN = (25, 68, 34)
tile_size = 20

soldier = pygame.image.load(consts.SOLDIER_NIGTH_IMG)
mine = pygame.image.load(consts.MINE_IMG)

def create_x_ray_board(real_matrix,soldier_location):
    x_ray_screen = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
    x_ray_screen.fill(BG)
    for y in range(0, consts.GRID_ROWS * 20, tile_size):
        pygame.draw.lines(x_ray_screen, GREEN, True, ((0, y), (consts.WINDOW_WIDTH, y)))

    for x in range(0, consts.GRID_COLUMNS * 20, tile_size):
        pygame.draw.lines(x_ray_screen, GREEN, True, ((x, 0), (x, consts.WINDOW_HEIGHT)))

    x_ray_screen.blit(soldier,soldier_location)

    for row in real_matrix:
        for col in row:
            if col == "mine" and (row.index(col)+1) == "mine" and (row.index(col)+2) == "mine":
                x_ray_screen.blit(mine,(real_matrix.index(row),row.index(col)))

create_x_ray_board(matrix,(20,20))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()

