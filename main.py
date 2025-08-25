import pygame
import sys
import time

state={
    "soldier_exploded":False,
    "reached_flag":False,
    "game_running":True,
    "soldier_location":[0,0]
}


def soldier_new_location(location):
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_DOWN:
                location[1]=location[1]+1
                print("hy")
            if event.key==pygame.K_RIGHT:
                location[0]=location[0]+1
                print("zet")
            if event.key==pygame.K_LEFT:
                location[0]=location[0]-1
                print("ct")
            if event.key==pygame.K_UP:
                location[1]=location[1]-1
                print("fceta")
            elif event.key==pygame.K_KP_ENTER or event.key==pygame.K_RETURN:
                pygame.display.update()
                time.sleep(1)
    return location




