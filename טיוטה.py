import consts
import pygame
import random
BG = (6, 13, 4)
GREEN = (21, 63, 31)
tile_size = consts.WINDOW_HEIGHT//consts.GRID_ROWS

soldier = pygame.image.load(consts.SOLDIER_NIGTH_IMG)
mine = pygame.image.load(consts.MINE_IMG)

EMPTY = "empty"
MINE = "mine"

def flag_idx(grid):
    for i in range(21,24):
        for j in range(46-50):
            grid[i][j]=consts.FLAG
    return grid


def game_grid(rows_length,cols_length):
    grid=[]
    for row in range(rows_length):
        row=[]
        for col in range(cols_length):
            col="empty"
            row.append(col)
        grid.append(row)

    return grid

def random_mines(grid):
    rows_range = range(0, consts.GRID_ROWS)
    cols_range = range(0, consts.GRID_COLUMNS - 2)
    rows = list(rows_range)
    cols = list(cols_range)
    counter=0
    while counter!=20:
        row_choice = random.choice(rows)
        col_choice = random.choice(cols)
        if grid[row_choice][col_choice]==consts.EMPTY and grid[row_choice][col_choice+1]==consts.EMPTY and grid[row_choice][col_choice+2]==consts.EMPTY and grid[row_choice][col_choice]!=[24,46] and grid[row_choice][col_choice]!=[24,47]:
            grid[row_choice][col_choice]=consts.MINE
            grid[row_choice][col_choice+1] = consts.MINE
            grid[row_choice][col_choice+2] = consts.MINE
            counter+=1

    return grid

def create_x_ray_board(real_matrix,soldier_location):
    x_ray_screen = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
    x_ray_screen.fill(BG)
    for y in range(0, consts.GRID_ROWS * 20, tile_size):
        pygame.draw.lines(x_ray_screen, GREEN, True, ((0, y), (consts.WINDOW_WIDTH, y)))

    for x in range(0, consts.GRID_COLUMNS * 20, tile_size):
        pygame.draw.lines(x_ray_screen, GREEN, True, ((x, 0), (x, consts.WINDOW_HEIGHT)))

    x_ray_screen.blit(soldier,soldier_location)

    for row in range(len(real_matrix)):
        for col in range(len(real_matrix[row])-2):
            if real_matrix[row][col] == "mine" and real_matrix[row][col+1] == "mine" and real_matrix[row][col+2] == "mine" and real_matrix[row][col+3] != "mine":
                x_ray_screen.blit(mine,(col*tile_size,row*tile_size))

grid = game_grid(25,50)
grid = flag_idx(grid)
grid = (random_mines(grid))
print(grid)
create_x_ray_board(grid,(0,0))


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()


