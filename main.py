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

CHEF_IMAGE = pygame.image.load(os.path.join('Assets', 'Chef2.gif'))
CHEF_SPRITE = pygame.transform.scale(CHEF_IMAGE, (CHEF_WIDTH, CHEF_HEIGHT))

BOMB_IMAGE = pygame.image.load(os.path.join('Assets', 'bomb.png'))
BOMB_SPRITE = pygame.transform.scale(BOMB_IMAGE, (BOMB_WIDTH, BOMB_HEIGHT))

ORANGE_IMAGE = pygame.image.load(os.path.join('Assets', 'orange.png'))
ORANGE_SPRITE = pygame.transform.scale(ORANGE_IMAGE, (ORANGE_WIDTH, ORANGE_HEIGHT))

BG_IMAGE = pygame.image.load(os.path.join('Assets', 'kitchen_floor.png'))

class Fruit:
    def __init__(self, image, width, height, speed):
        self.x = WIDTH
        self.y = randrange(HEIGHT)
        self.image = pygame.transform.scale(image, (width, height))
        self.speed = speed

    def move(self):
        self.x -= self.speed
        if self.x <= 0:
            self.x = WIDTH
            self.y = randrange(HEIGHT)

    def draw(self):
        WIN.blit(self.image, (self.x, self.y))

class Bomb:
    def __init__(self, image, width, height, speed):
        self.x = WIDTH
        self.y = randrange(HEIGHT)
        self.image = pygame.transform.scale(image, (width, height))
        self.speed = speed

    def move(self):
        self.x -= self.speed
        if self.x <= 0:
            self.x = WIDTH
            self.y = randrange(HEIGHT)

    def draw(self):
        WIN.blit(self.image, (self.x, self.y))

def draw_window(chef_position, bomb, orange):
    WIN.blit(BG_IMAGE, (0, 0))
    WIN.blit(CHEF_SPRITE, (chef_position.x, chef_position.y))
    bomb.draw()
    orange.draw()
    pygame.display.update()

def main():
    chef_position = pygame.Rect(100, 200, CHEF_WIDTH, CHEF_HEIGHT)
    bomb = Bomb(BOMB_IMAGE, BOMB_WIDTH, BOMB_HEIGHT, 5)
    orange = Fruit(ORANGE_IMAGE, ORANGE_WIDTH, ORANGE_HEIGHT, 3)

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_a]:
            chef_position.x -= VEL
        if keys_pressed[pygame.K_d]:
            chef_position.x += VEL
        if keys_pressed[pygame.K_w]:
            chef_position.y -= VEL
        if keys_pressed[pygame.K_s]:
            chef_position.y += VEL

        bomb.move()
        orange.move()

        draw_window(chef_position, bomb, orange)

    pygame.quit()

if __name__ == "__main__":
    main()
