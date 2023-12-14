import pygame
import os

WIDTH, HEIGHT = 900, 500
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
ORANGE_SPRITE= pygame.transform.scale(ORANGE_IMAGE,(ORANGE_WIDTH, ORANGE_HEIGHT))

def draw_window(chef_position, bomb_position, orange_position):
    WIN.fill((66, 245, 233))
    WIN.blit(CHEF_SPRITE, (chef_position.x, chef_position.y))
    WIN.blit(BOMB_SPRITE,(bomb_position.x, bomb_position.y))
    WIN.blit(ORANGE_SPRITE,(orange_position.x, orange_position.y) )
    pygame.display.update()

def main():
    bomb_position =pygame.Rect(900,200, BOMB_WIDTH, BOMB_HEIGHT)
    chef_position =pygame.Rect(100,200, CHEF_WIDTH, CHEF_HEIGHT)
    orange_position = pygame.Rect(900, 250, ORANGE_WIDTH, ORANGE_HEIGHT)


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

        bomb_position.x -= 3
        orange_position.x -= 3

        draw_window(chef_position, bomb_position, orange_position)

    pygame.quit()

if __name__ == "__main__":
    main()