import pygame
import os
from random import randrange



WIDTH, HEIGHT = 900, 495
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Citrus Slicer!")

FPS = 60
VEL = 5

CHEF_WIDTH, CHEF_HEIGHT = 70, 90
BOMB_WIDTH, BOMB_HEIGHT = 50, 50
ORANGE_WIDTH, ORANGE_HEIGHT = 35, 35

CHEF_IMAGE = pygame.image.load(os.path.join('Assets','Chef2.gif'))
CHEF_SPRITE = pygame.transform.scale(CHEF_IMAGE, (CHEF_WIDTH, CHEF_HEIGHT))

BOMB_IMAGE = pygame.image.load(os.path.join('Assets','bomb.png'))
BOMB_SPRITE = pygame.transform.scale(BOMB_IMAGE, (BOMB_WIDTH, BOMB_HEIGHT))

ORANGE_IMAGE = pygame.image.load(os.path.join('Assets','orange.png'))
ORANGE_SPRITE = pygame.transform.scale(ORANGE_IMAGE,(ORANGE_WIDTH, ORANGE_HEIGHT))

BG_IMAGE = pygame.image.load(os.path.join('Assets','kitchen_floor.png'))

fruit_x = 900
fruit_y = randrange(HEIGHT)

bomb_x = 900
bomb_y = randrange(HEIGHT)

game_display = pygame.display.set_mode((WIDTH, HEIGHT))

class Fruit:
    fruit_x = 900
    fruit_y = randrange(HEIGHT)
    #use class to set up everything the current orange is doing, use time interval to spawn fruits from an array, for loop for iterating through array at random.
#class Bomb:
#Class Chef: probably needed for hit detection. 



def draw_window(chef_position, bomb_x, bomb_y, fruit_x, fruit_y):
    WIN.blit(BG_IMAGE,(0,0))
    WIN.blit(CHEF_SPRITE, (chef_position.x, chef_position.y))
    WIN.blit(BOMB_SPRITE, (bomb_x, bomb_y))
    # WIN.blit(ORANGE_SPRITE, (fruit_x, fruit_y))
    pygame.display.update()


def main():
    
    chef_position =pygame.Rect(100,200, CHEF_WIDTH, CHEF_HEIGHT)
    bomb_x = 900
    bomb_y = randrange(HEIGHT)
    fruit_x = 900
    fruit_y = randrange(HEIGHT)


    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_a]: #left
            chef_position.x -= VEL
        if keys_pressed[pygame.K_d]: #right
            chef_position.x += VEL
        if keys_pressed[pygame.K_w]: #up
            chef_position.y -= VEL
        if keys_pressed[pygame.K_s]: #down
            chef_position.y += VEL
        
        #REPLACE BELOW WITH A METHOD HOUSED IN THE FRUIT CLASS.
        #Fruit list: spawn on right side, move across screen, despawn at end of screen.
        # create function to spawn the fruit on ride sight(900) at random intervals at a random y value.  
        # do the same for bombs
        bomb_x -= 5
        if bomb_x <= 0:
            bomb_x = 900
            bomb_y = randrange(HEIGHT)

        fruit_x -= 3
        if fruit_x <= 0:
            fruit_x = 900
            fruit_y = randrange(HEIGHT)

        draw_window(chef_position, bomb_x, bomb_y, fruit_x, fruit_y)
        

    pygame.quit()

if __name__ == "__main__":
    main()