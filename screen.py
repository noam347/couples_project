import pygame
import consts
import random




pygame.init()
screen = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
pygame.display.set_caption('The flag')
screen.fill(consts.BACKGROUND_COLOR)
pygame.display.flip()
    # return screen



grass = pygame.image.load(consts.GRASS_IMG)
# grass_height = consts.WINDOW_HEIGHT//consts.GRID_COLUMNS
# print(grass_height)
# grass_width = consts.WINDOW_WIDTH//consts.GRID_ROWS
# print(grass_width)
# # pygame.transform.scale(grass,(grass_width,grass_height))
# pygame.transform.scale(grass,(750,500))


def randomize_grass_location():
    x_location = random.randrange(0, consts.WINDOW_WIDTH-60)
    y_location = random.randrange(0, consts.WINDOW_HEIGHT-60)
    return  x_location,y_location


def add_grass():
    for i in range(20):
        screen.blit(grass, (randomize_grass_location()))

add_grass()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
