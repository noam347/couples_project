import consts
import pygame
BG = (6, 13, 4)
GREEN = (21, 63, 31)
tile_size = consts.WINDOW_HEIGHT//consts.GRID_ROWS

soldier = pygame.image.load(consts.SOLDIER_NIGTH_IMG)
mine = pygame.image.load(consts.MINE_IMG)

EMPTY = "empty"
MINE = "mine"

matrix = [[EMPTY,EMPTY,EMPTY,MINE,MINE,MINE,EMPTY,EMPTY,EMPTY,MINE,MINE,MINE,EMPTY,EMPTY,EMPTY,MINE,MINE,MINE,EMPTY,EMPTY,EMPTY,MINE,MINE,MINE,EMPTY,EMPTY,EMPTY,MINE,MINE,MINE,EMPTY,EMPTY,EMPTY,MINE,MINE,MINE],
            [EMPTY,EMPTY,EMPTY,MINE,MINE,MINE,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,MINE,MINE,MINE,EMPTY,EMPTY,EMPTY,MINE,MINE,MINE,EMPTY,EMPTY,EMPTY,MINE,MINE,MINE,EMPTY,EMPTY,EMPTY,MINE,MINE,MINE,EMPTY,MINE,MINE,MINE]]

def create_x_ray_board(real_matrix,soldier_location):
    x_ray_screen = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
    x_ray_screen.fill(BG)
    for y in range(0, consts.GRID_ROWS * 20, tile_size):
        pygame.draw.lines(x_ray_screen, GREEN, True, ((0, y), (consts.WINDOW_WIDTH, y)))

    for x in range(0, consts.GRID_COLUMNS * 20, tile_size):
        pygame.draw.lines(x_ray_screen, GREEN, True, ((x, 0), (x, consts.WINDOW_HEIGHT)))

    x_ray_screen.blit(soldier,soldier_location)

    for row in range(len(real_matrix)):
        print(real_matrix[row])
        for col in range(len(real_matrix[row])-2):
            print(real_matrix[row][col])
            if real_matrix[row][col] == "mine" and real_matrix[row][col+1] == "mine" and real_matrix[row][col+2] == "mine":
                x_ray_screen.blit(mine,(col*tile_size,row*tile_size))

create_x_ray_board(matrix,(0,0))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()


