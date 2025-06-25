import pygame
import random
import sys
import math

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

YELLOW = (255, 255, 0)

# プレイヤークラス
class Player:
    def __init__(self):
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        self.size = 40
        self.speed = 5

    def draw(self):
        side = self.size
        height = (math.sqrt(3)/2)*side
        points = [
            (self.x, self.y - height / 2),
            (self.x - side / 2, self.y + height / 2),
            (self.x + side / 2, self.y + height / 2)
        ]
        pygame.draw.polygon(screen, YELLOW, points)

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.x > self.size/2:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] and self.x < WIDTH - self.size/2:
            self.x += self.speed

# オブジェクト生成
player = Player()

while True:
    screen.fill((0, 0, 0))
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    player.move(keys)
    player.draw()

    pygame.display.flip()
    clock.tick(60)
