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
        self.hitbox_scale_horizontal = 0.70
        self.hitbox_scale_vertical = 0.60
        self.hitbox_width = int(self.width * self.hitbox_scale_horizontal)
        self.hitbox_height = int(self.height * self.hitbox_scale_vertical)
        self.hitbox = pygame.Rect(self.x + (self.width - self.hitbox_width) // 2, self.y + (self.height - self.hitbox_height) // 2, self.hitbox_width, self.hitbox_height)
        self.score = 0
        self.lives = 3
        self.game_over = False

    def move(self, keys_pressed):
        if not self.game_over:
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

    def lose_life(self):
        self.lives -= 1
        if self.lives == 0:
            self.game_over = True

class Fruit:
    def __init__(self, images, width, height, speed, points):
        self.x = WIDTH
        self.y = randrange(HEIGHT)
        self.images = [pygame.transform.scale(img, (width, height)) for img in images]
        self.image = choice(self.images)
        self.speed = speed
        self.points = choice(points)
        self.spawn_timer = uniform(0.25, 0.5)
        self.fruits_on_screen = []
        self.hitbox = pygame.Rect(self.x, self.y, width, height)

    def move(self):
        self.x -= self.speed
        if self.x <= 0:
            self.x = WIDTH
            self.y = randrange(HEIGHT)
        self.hitbox = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())

    def spawn_fruit(self, chef):
        if not chef.game_over and len(self.fruits_on_screen) < 10:
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

    def spawn_bomb(self, chef):
        if not chef.game_over and len(self.bombs_on_screen) < 5:
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
    WIN.blit(score_text, (WIDTH - score_text.get_width() - 10, 10))
    if not chef.game_over:
        for i in range(chef.lives):
            pygame.draw.circle(WIN, (0, 255, 0), (int(WIDTH / 2) - 30 * i, 30), 15)
    else:
        font = pygame.font.Font(None, 74)
        game_over_text = font.render("GAME OVER", True, (255, 0, 0))
        WIN.blit(game_over_text, ((WIDTH - game_over_text.get_width()) // 2, HEIGHT // 3))
    pygame.display.update()

def draw_start_screen():
    WIN.blit(BG_IMAGE, (0, 0))
    font_title = pygame.font.Font(None, 74)
    title_text = font_title.render("CITRUS SLICER", True, (255, 165, 0))  # Orange color
    WIN.blit(title_text, ((WIDTH - title_text.get_width()) // 2, HEIGHT // 3))

    # Draw start button
    pygame.draw.rect(WIN, (0, 255, 0), (WIDTH // 2 - 75, HEIGHT // 2, 150, 50))  # Green color
    font_button = pygame.font.Font(None, 36)
    button_text = font_button.render("START", True, (0, 0, 0))  # Black color
    WIN.blit(button_text, ((WIDTH - button_text.get_width()) // 2, HEIGHT // 2 + 10))

    pygame.display.update()

def check_collision(chef, bomb, fruit):
    for fruit_instance in fruit.fruits_on_screen[:]:
        if chef.hitbox.colliderect(fruit_instance.hitbox):
            chef.score += fruit_instance.points
            fruit.fruits_on_screen.remove(fruit_instance)

    for bomb_instance in bomb.bombs_on_screen[:]:
        if chef.hitbox.colliderect(bomb_instance.hitbox):
            chef.lives -= 1
            bomb.bombs_on_screen.remove(bomb_instance)

def main():
    chef = Chef(100, 200)
    bomb = Bomb(BOMB_IMAGE, BOMB_WIDTH, BOMB_HEIGHT, 5)
    fruit = Fruit([ORANGE_IMAGE, WATERMELON_IMAGE, STRAWBERRY_IMAGE, PINEAPPLE_IMAGE, BANANA_IMAGE], 38, 38, 3, [10, 20, 5, 15, 15])

    clock = pygame.time.Clock()
    start_screen = True

    while start_screen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                start_screen = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if WIDTH // 2 - 75 <= x <= WIDTH // 2 + 75 and HEIGHT // 2 <= y <= HEIGHT // 2 + 50:
                    start_screen = False

        draw_start_screen()

    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed()
        chef.move(keys_pressed)

        if chef.lives > 0:
            bomb.move()
            fruit.move()

            bomb.spawn_timer -= 1 / FPS
            fruit.spawn_timer -= 1 / FPS

            if bomb.spawn_timer <= 0:
                bomb.spawn_bomb(chef)
                bomb.spawn_timer = uniform(0.25, 0.5)

            if fruit.spawn_timer <= 0:
                fruit.spawn_fruit(chef)
                fruit.spawn_timer = uniform(0.25, 0.5)

            check_collision(chef, bomb, fruit)
        else:
            fruit.fruits_on_screen = []
            bomb.bombs_on_screen = []

        draw_window(chef, bomb, fruit)

        if chef.lives <= 0:
            font = pygame.font.Font(None, 74)
            game_over_text = font.render("GAME OVER", True, (255, 0, 0))
            WIN.blit(game_over_text, ((WIDTH - game_over_text.get_width()) // 2, HEIGHT // 3))
            pygame.display.update()
            pygame.time.delay(3000)  # Display "GAME OVER" for 3 seconds
            run = False

    pygame.quit()

if __name__ == "__main__":
    main()
