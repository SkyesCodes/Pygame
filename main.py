import pygame
import os
from random import randrange, uniform

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
        self.spawn_timer = uniform(0.25, 0.5)  # Random initial timer
        self.fruits_on_screen = []

    def move(self):
        self.x -= self.speed
        if self.x <= 0:
            self.x = WIDTH
            self.y = randrange(HEIGHT)

    def spawn_fruit(self):
        if len(self.fruits_on_screen) < 10:
            self.fruits_on_screen.append(Fruit(ORANGE_IMAGE, ORANGE_WIDTH, ORANGE_HEIGHT, 3))

    def draw(self):
        for fruit in self.fruits_on_screen:
            fruit.move()
            WIN.blit(fruit.image, (fruit.x, fruit.y))

class Bomb:
    def __init__(self, image, width, height, speed):
        self.x = WIDTH
        self.y = randrange(HEIGHT)
        self.image = pygame.transform.scale(image, (width, height))
        self.speed = speed
        self.spawn_timer = uniform(0.25, 0.5)  # Random initial timer
        self.bombs_on_screen = []

    def move(self):
        self.x -= self.speed
        if self.x <= 0:
            self.x = WIDTH
            self.y = randrange(HEIGHT)

    def spawn_bomb(self):
        if len(self.bombs_on_screen) < 5:
            self.bombs_on_screen.append(Bomb(BOMB_IMAGE, BOMB_WIDTH, BOMB_HEIGHT, 5))

    def draw(self):
        for bomb in self.bombs_on_screen:
            bomb.move()
            WIN.blit(bomb.image, (bomb.x, bomb.y))

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

        bomb.spawn_timer -= 1 / FPS
        orange.spawn_timer -= 1 / FPS

        if bomb.spawn_timer <= 0:
            bomb.spawn_bomb()
            bomb.spawn_timer = uniform(0.25, 0.5)

        if orange.spawn_timer <= 0:
            orange.spawn_fruit()
            orange.spawn_timer = uniform(0.25, 0.5)

        draw_window(chef_position, bomb, orange)

    pygame.quit()

if __name__ == "__main__":
    main()
