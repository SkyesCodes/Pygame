import pygame
import os

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Citrus Slicer!")

FPS = 60
VEL = 5

CHEF_WIDTH, CHEF_HEIGHT = 80, 100

CHEF_IMAGE = pygame.image.load(os.path.join('Assets','chef-gif.gif'))
CHEF_SPRITE = pygame.transform.scale(CHEF_IMAGE, (CHEF_WIDTH, CHEF_HEIGHT))

def draw_window(chef_position):
    WIN.fill((66, 245, 233))
    WIN.blit(CHEF_SPRITE, (chef_position.x, chef_position.y))
    pygame.display.update()

def main():
    chef_position =pygame.Rect(100,200, CHEF_WIDTH, CHEF_HEIGHT)



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

        draw_window(chef_position)

    pygame.quit()

if __name__ == "__main__":
    main()