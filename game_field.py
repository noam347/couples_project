import pygame
import main
import consts
import soldier
import random


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
    while counter!=60:
        row_choice = random.choice(rows)
        col_choice = random.choice(cols)
        if grid[row_choice][col_choice]==consts.EMPTY and grid[row_choice][col_choice+1]==consts.EMPTY and grid[row_choice][col_choice+2]==consts.EMPTY and grid[row_choice][col_choice+1]!=[24,46] and grid[row_choice][col_choice+1]!=[24,47]:
            grid[row_choice][col_choice]=consts.MINE
    return grid

def flag_idx(grid):
    for i in range(21,24):
        for j in range(46-50):
            grid[i][j]=consts.FLAG
    return grid


def flag_related_index():
    for row in consts.FLAG_IDX:
        for col in consts.FLAG_IDX[row]:



def flag_reaching(location):
    check=False
    soldier_place=soldier.soldier_body(location)
    for row in consts.FLAG_IDX:
        for col in consts.FLAG_IDX[row]:
            for i in soldier_place:
                for j in soldier_place[row]:
                    if row==i-1 and col==j-1:
                        check=True
    return check

def explosion(location):

