import pygame
import random
import sys
import math

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Sample")
clock = pygame.time.Clock()

YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

class Player:
    def __init__(self):
        self.x = WIDTH // 2
        self.y = HEIGHT - 50
        self.size = 40
        self.speed = 5

    def draw(self):
        side = self.size
        height = (math.sqrt(3) / 2) * side
        
        # 三角形の頂点座標を計算（上向きの正三角形を想定）
        points = [
            (self.x, self.y - height / 2),           # 上の頂点
            (self.x - side / 2, self.y + height / 2), # 左下の頂点
            (self.x + side / 2, self.y + height / 2)  # 右下の頂点
        ]
        pygame.draw.polygon(screen, YELLOW, points)

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.x > self.size / 2:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] and self.x < WIDTH - self.size / 2:
            self.x += self.speed

class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.r = 5
        self.vy = 7

    def draw(self):
        pygame.draw.circle(screen, BLUE, (self.x, self.y), self.r)

    def move(self):
        self.y -= self.vy # ここが `self.y -= self.y` になっていました。速度 `self.vy` で移動するように修正

class Enemy:
    def __init__(self):
        self.size = 30
        self.reset()

    def reset(self):
        self.x = random.randint(50, WIDTH - 50)
        self.y = random.randint(-150, -50)
        self.vy = 2

    def move(self):
        self.y += self.vy
        if self.y > HEIGHT:
            self.reset()

    def draw(self):
        pygame.draw.rect(screen, RED, (self.x, self.y, self.size, self.size))

player = Player()
bullets = []
enemies = [Enemy() for _ in range(5)]

while True:
    screen.fill(BLACK)

    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            bullets.append(Bullet(player.x, player.y - player.size // 2))

    player.move(keys)
    player.draw()

    # 弾丸の更新と描画、および画面外に出た弾丸の削除
    # リストをループ中に要素を削除するとスキップが発生するため、コピーに対してループします
    for b in bullets[:]:
        b.move()
        b.draw()
        if b.y < -b.r:
            bullets.remove(b)

    # 敵の更新と描画
    for e in enemies:
        e.move()
        e.draw()

    # 衝突判定
    # 衝突時にリストから要素を削除するため、コピーに対してループします
    for e in enemies[:]:
        ex, ey = e.x + e.size // 2, e.y + e.size // 2 # 敵の中心座標
        for b in bullets[:]:
            # 弾丸の中心座標
            bx, by = b.x, b.y
            if math.hypot(ex - bx, ey - by) < e.size // 2 + b.r:
                enemies.remove(e)
                bullets.remove(b)
                # 衝突した敵は削除されたので、その敵に対する弾丸のループは不要
                # 新しい敵を生成するロジックがないため、ここではそのまま
                # 必要であれば `enemies.append(Enemy())` などで追加
                enemies.append(Enemy()) # 敵を倒したら新しい敵を生成
                break # 1つの敵に複数の弾丸が当たらないように、弾丸のループを抜ける

    pygame.display.flip()
    clock.tick(60)