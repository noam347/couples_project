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
    "soldier_location":None
}

def main():
    pygame.init()
    grass_locations = screen.randomize_grass_location()
    game_screen = screen.create_regular_screen(grass_locations)
    screen.updated_location(game_screen,soldier.soldier_start_position)
    screen.draw_start_message(game_screen)
    grid=game_field.game_grid(consts.GRID_ROWS,consts.GRID_COLUMNS)
    state["soldier_location"]=soldier.soldier_start_position
    while state["game_running"]:
        soldier_location=soldier_new_location(game_screen,grass_locations,grid,state["soldier_location"])
        #soldier_location=soldier.soldier_location_grid(state["soldier_location"])
        if game_field.flag_reaching(soldier_location,grid):
            state["reached_flag"]=True
        elif game_field.explosion(soldier_location,grid):
            state["soldier_exploded"]=True
        if state["reached_flag"]:
            print("you won!")
            screen.draw_win_message(game_screen)
            time.sleep(3)
            state["game_running"]=False
        elif state["soldier_exploded"]:
            print("you exploded")
            screen.draw_lose_message(game_screen)
            time.sleep(3)
            state["game_running"] = False


def soldier_new_location(game_screen,grass_locations,grid,location):
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_DOWN:
                if location[1] >= 420:
                    pass
                else:
                    location[1]=location[1]+20
                    screen.create_regular_screen(grass_locations)
                    screen.updated_location(game_screen, location)
            elif event.key==pygame.K_RIGHT:
                if location[0] >=940:
                    pass
                else:
                    location[0]=location[0]+20
                    screen.create_regular_screen(grass_locations)
                    screen.updated_location(game_screen, location)
            elif event.key==pygame.K_LEFT:
                if location[0] ==-20:
                    pass
                else:
                    location[0] = location[0] - 20
                    screen.create_regular_screen(grass_locations)
                    screen.updated_location(game_screen, location)
            elif event.key==pygame.K_UP:
                if location[1] ==0:
                    pass
                else:
                    location[1]=location[1]-20
                    screen.create_regular_screen(grass_locations)
                    screen.updated_location(game_screen, location)
            elif event.key==pygame.K_KP_ENTER or event.key==pygame.K_RETURN:
                screen.create_x_ray_board(grid,state["soldier_location"])
                time.sleep(1)
                screen.create_regular_screen(grass_locations)
                screen.updated_location(game_screen,location)
    return location


if __name__ == '__main__':
    main()
