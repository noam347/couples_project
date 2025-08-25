import pygame
import sys
import consts
import screen
import game_field
import soldier


state={
    "soldier_exploded":False,
    "reached_flag":False,
    "game_running":True,
    "soldier_location":soldier.soldier_start_position
}



def main():


def soldier_new_location(location):
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_DOWN:
                location[1]=location[1]+1
            if event.key==pygame.K_RIGHT:
                location[0]=location[0]+1
            if event.key==pygame.K_LEFT:
                location[0]=location[0]-1
            if event.key==pygame.K_UP:
                location[1]=location[1]-1


