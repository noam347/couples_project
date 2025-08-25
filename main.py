import pygame
import sys
import consts
import screen
import game_field
import soldier
import time

state={
    "soldier_exploded":False,
    "reached_flag":False,
    "game_running":True,
    "soldier_location":soldier.soldier_start_position
}

def main():
    grid=game_field.game_grid(consts.GRID_ROWS,consts.GRID_COLUMNS)
    soldier_location=state["soldier_location"]
    flag_location=game_field.flag_related_index(grid)
    mines_location=game_field.mine_related_index(grid)
    while state["game_running"]:
        soldier_location=soldier_new_location(soldier_location)
        if game_field.flag_reaching(soldier_location,grid):
            state["reached_flag"]=True
        elif game_field.explosion(soldier_location,grid):
            state["soldier_location"]=True
        if state["reached_flag"]:
            print("you won")
            time.sleep(3)
            state["game_running"]=False
        elif state["soldier_exploded"]:
            print("you lose")
            time.sleep(3)
            state["game_running"] = False





grid = game_field.game_grid(consts.GRID_ROWS,consts.GRID_COLUMNS)
grid = game_field.flag_idx(grid)
grid = game_field.random_mines(grid)
print(grid)


def soldier_new_location(location):
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_DOWN:
                location[1]=location[1]+1
                print("hy")
            elif event.key==pygame.K_RIGHT:
                location[0]=location[0]+1
                print("zet")
            elif event.key==pygame.K_LEFT:
                location[0]=location[0]-1
                print("ct")
            elif event.key==pygame.K_UP:
                location[1]=location[1]-1
                print("fceta")
            elif event.key==pygame.K_KP_ENTER or event.key==pygame.K_RETURN:
                screen.create_x_ray_board(grid,state["soldier_location"])
                time.sleep(1)
    return location


