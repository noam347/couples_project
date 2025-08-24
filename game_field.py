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
    for i in range(19):
        rows_range=range(0,consts.GRID_ROWS)
        cols_range=range(0,consts.GRID_COLUMNS-2)
        rows=list(rows_range)
        cols=list(cols_range)
        row_choice=random.choice(rows)
        col_choice=random.choice(cols)
        grid[row_choice][col_choice]="mine"
        rows.remove(row_choice)
        del cols[col_choice:col_choice+2]
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

