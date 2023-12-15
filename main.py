import pygame
import os
from random import randrange, uniform, choice

WIDTH, HEIGHT = 900, 495
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Citrus Slicer!")

FPS = 60
VEL = 5

CHEF_WIDTH, CHEF_HEIGHT = 70, 90
BOMB_WIDTH, BOMB_HEIGHT = 50, 50

ORANGE_WIDTH, ORANGE_HEIGHT = 32, 32
WATERMELON_WIDTH, WATERMELON_HEIGHT = 40, 40
PINEAPPLE_WIDTH, PINEAPPLE_HEIGHT = 38, 38
BANANA_WIDTH, BANANA_HEIGHT = 38, 38
STRAWBERRY_WIDTH, STRAWBERRY_HEIGHT = 25, 25

CHEF_IMAGE = pygame.image.load(os.path.join('Assets', 'Chef2.gif'))
CHEF_SPRITE = pygame.transform.scale(CHEF_IMAGE, (CHEF_WIDTH, CHEF_HEIGHT))

BOMB_IMAGE = pygame.image.load(os.path.join('Assets', 'bomb.png'))
BOMB_SPRITE = pygame.transform.scale(BOMB_IMAGE, (BOMB_WIDTH, BOMB_HEIGHT))

BG_IMAGE = pygame.image.load(os.path.join('Assets', 'kitchen_floor.png'))

ORANGE_IMAGE = pygame.image.load(os.path.join('Assets', 'orange.png'))
WATERMELON_IMAGE = pygame.image.load(os.path.join('Assets', 'watermelon.png'))
STRAWBERRY_IMAGE = pygame.image.load(os.path.join('Assets', 'strawberry.png'))
PINEAPPLE_IMAGE = pygame.image.load(os.path.join('Assets', 'pineapple.png'))
BANANA_IMAGE = pygame.image.load(os.path.join('Assets', 'banana.png'))

pygame.font.init()  # Initialize the font module

class Chef:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = CHEF_WIDTH
        self.height = CHEF_HEIGHT
        self.hitbox_scale_horizontal = 0.80
        self.hitbox_scale_vertical = 0.70
        self.hitbox_width = int(self.width * self.hitbox_scale_horizontal)
        self.hitbox_height = int(self.height * self.hitbox_scale_vertical)
        self.hitbox = pygame.Rect(self.x + (self.width - self.hitbox_width) // 2, self.y + (self.height - self.hitbox_height) // 2, self.hitbox_width, self.hitbox_height)
        self.score = 0

    def move(self, keys_pressed):
        if keys_pressed[pygame.K_a]:
            self.x -= VEL
        if keys_pressed[pygame.K_d]:
            self.x += VEL
        if keys_pressed[pygame.K_w]:
            self.y -= VEL
        if keys_pressed[pygame.K_s]:
            self.y += VEL
        self.hitbox = pygame.Rect(self.x + (self.width - self.hitbox_width) // 2, self.y + (self.height - self.hitbox_height) // 2, self.hitbox_width, self.hitbox_height)

    def draw(self):
        WIN.blit(CHEF_SPRITE, (self.x, self.y))

class Fruit:
    def __init__(self, images, width, height, speed, points):
        self.x = WIDTH
        self.y = randrange(HEIGHT)
        self.images = [pygame.transform.scale(img, (width, height)) for img in images]
        self.image = choice(self.images)
        self.speed = speed
        self.points = points
        self.spawn_timer = uniform(0.25, 0.5)
        self.fruits_on_screen = []
        self.hitbox = pygame.Rect(self.x, self.y, width, height)

    def move(self):
        self.x -= self.speed
        if self.x <= 0:
            self.x = WIDTH
            self.y = randrange(HEIGHT)
        self.hitbox = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())

    def spawn_fruit(self):
        if len(self.fruits_on_screen) < 10:
            self.fruits_on_screen.append(Fruit([ORANGE_IMAGE, WATERMELON_IMAGE, STRAWBERRY_IMAGE, PINEAPPLE_IMAGE, BANANA_IMAGE], 38, 38, 3, [10, 20, 5, 15, 15]))

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
        self.spawn_timer = uniform(0.25, 0.5)
        self.bombs_on_screen = []
        self.hitbox = pygame.Rect(self.x, self.y, width, height)

    def move(self):
        self.x -= self.speed
        if self.x <= 0:
            self.x = WIDTH
            self.y = randrange(HEIGHT)
        self.hitbox = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())

    def spawn_bomb(self):
        if len(self.bombs_on_screen) < 5:
            self.bombs_on_screen.append(Bomb(BOMB_IMAGE, BOMB_WIDTH, BOMB_HEIGHT, 5))

    def draw(self):
        for bomb in self.bombs_on_screen:
            bomb.move()
            WIN.blit(bomb.image, (bomb.x, bomb.y))

def draw_window(chef, bomb, fruit):
    WIN.blit(BG_IMAGE, (0, 0))
    chef.draw()
    bomb.draw()
    fruit.draw()
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {chef.score}", True, (255, 255, 255))
    WIN.blit(score_text, (WIDTH - 150, 10))
    pygame.display.update()

def check_collision(chef, bomb, fruit):
    chef_rect = pygame.Rect(chef.hitbox.x, chef.hitbox.y, chef.hitbox.width, chef.hitbox.height)
    for bomb_instance in bomb.bombs_on_screen:
        bomb_rect = pygame.Rect(bomb_instance.hitbox.x, bomb_instance.hitbox.y, bomb_instance.hitbox.width, bomb_instance.hitbox.height)
        if chef_rect.colliderect(bomb_rect):
            bomb.bombs_on_screen.remove(bomb_instance)

    for fruit_instance in fruit.fruits_on_screen:
        fruit_rect = pygame.Rect(fruit_instance.hitbox.x, fruit_instance.hitbox.y, fruit_instance.hitbox.width, fruit_instance.hitbox.height)
        if chef_rect.colliderect(fruit_rect):
            chef.score += fruit_instance.points[fruit_instance.images.index(fruit_instance.image)]
            fruit.fruits_on_screen.remove(fruit_instance)

def main():
    chef = Chef(100, 200)
    bomb = Bomb(BOMB_IMAGE, BOMB_WIDTH, BOMB_HEIGHT, 5)
    fruit = Fruit([ORANGE_IMAGE, WATERMELON_IMAGE, STRAWBERRY_IMAGE, PINEAPPLE_IMAGE, BANANA_IMAGE], 38, 38, 3, [10, 20, 5, 15, 15])

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed()
        chef.move(keys_pressed)

        bomb.move()
        fruit.move()

        bomb.spawn_timer -= 1 / FPS
        fruit.spawn_timer -= 1 / FPS

        if bomb.spawn_timer <= 0:
            bomb.spawn_bomb()
            bomb.spawn_timer = uniform(0.25, 0.5)

        if fruit.spawn_timer <= 0:
            fruit.spawn_fruit()
            fruit.spawn_timer = uniform(0.25, 0.5)

        check_collision(chef, bomb, fruit)
        draw_window(chef, bomb, fruit)

    pygame.quit()

if __name__ == "__main__":
    main()
