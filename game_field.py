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
    grid=flag_idx(grid)
    grid=random_mines(grid)

    return grid



def random_mines(grid):
    rows_range = range(0, consts.GRID_ROWS)
    cols_range = range(0, consts.GRID_COLUMNS - 2)
    rows = list(rows_range)
    cols = list(cols_range)
    soldier_body=soldier.soldier_body(soldier.soldier_start_position)
    soldier_legs=soldier.soldier_legs(soldier.soldier_start_position)
    counter=0
    while counter!=20:
        row_choice = random.choice(rows)
        col_choice = random.choice(cols)
        if grid[row_choice][col_choice]==consts.EMPTY and grid[row_choice][col_choice+1]==consts.EMPTY and grid[row_choice][col_choice+2]==consts.EMPTY:
            if grid[row_choice][col_choice]!=[24,46] and grid[row_choice][col_choice]!=[24,47]:
                if [row_choice,col_choice] not in soldier_legs and [row_choice,col_choice] not in soldier_body:
                    grid[row_choice][col_choice]=consts.MINE
                    grid[row_choice][col_choice+1] = consts.MINE
                    grid[row_choice][col_choice+2] = consts.MINE
                    counter+=1

    return grid

def flag_idx(grid):
    for i in range(21,24):
        for j in range(46,50):
            grid[i][j]=consts.FLAG
    return grid

def flag_related_index(grid):
    list_flag_idx=[]
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col]==consts.FLAG:
                list_flag_idx.append(grid[row][col])
    return list_flag_idx

def mine_related_index(grid):
    list_mine_idx=[]
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col]==consts.MINE:
                list_mine_idx.append(grid[row][col])
    return list_mine_idx


def flag_reaching(location,grid):
    check=False
    soldier_place=soldier.soldier_body(location)
    idx_list=flag_related_index(grid)
    for idx in soldier_place:
        if idx in idx_list:
            check=True
    return check

def explosion(location,grid):
    check=False
    soldier_place=soldier.soldier_legs(location)
    idx_list=mine_related_index(grid)
    for idx in soldier_place:
        if idx in idx_list:
            check=True
    return check

print("ikik")


