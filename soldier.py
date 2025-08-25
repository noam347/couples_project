import pygame.image
import consts

soldier = pygame.image.load(consts.SOLDIER_IMG)
soldier_start_position = [0,0]

def soldier_body(location):
    row = location[0]
    col = location[1]
    soldiers_body= [[row,col],[row,col+1],[row+1,col],[row+1,col+1],[row+2,col],[row+2,col+1]]
    return soldiers_body

def soldier_legs(location):
    row = location[0]
    col = location[1]
    soldiers_legs = [[row+3, col], [row+3, col + 1]]
    return soldiers_legs

def soldier_within_boundaries(location):
    if location[0] == (consts.GRID_ROWS-4) and location[1] == (consts.GRID_COLUMNS-2):
        return True
    else:
        return False
