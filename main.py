import pygame
import os

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Citrus Slicer!")

FPS = 60

CHEF_IMAGE = pygame.image.load(os.path.join('Assets','chef-gif.gif'))
CHEF_SPRITE = pygame.transform.scale(CHEF_IMAGE, (80, 100))
def draw_window():
    WIN.fill((66, 245, 233))
    WIN.blit(CHEF_SPRITE, (300, 100))
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_window()

    pygame.quit()

if __name__ == "__main__":
    main()