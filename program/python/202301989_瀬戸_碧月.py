import pygame
import random

# Pygameの初期化
pygame.init()

# 画面設定
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("アクションゲーム")

# 色の定義
RED = (255, 0, 0) # プレイヤー
GREEN = (0, 255, 0) # 攻撃範囲
BLUE = (0, 0, 255) # 敵
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# フォントの設定
font = pygame.font.Font(None, 36)

# プレイヤーの設定
player_size = 50
player_speed = 5
player_attack_cooldown = 30 # 攻撃クールダウン 
current_attack_cooldown = 0
attack_duration = 10 # 攻撃アニメーションの持続時間 
current_attack_duration = 0

# 敵の設定
enemy_size = 30
enemy_speed = 3
MAX_ENEMIES = 5
ENEMY_SPAWN_INTERVAL = 60
spawn_counter = 0

# ゲームの状態変数
score = 0
player_life = 3
game_over = False

# プレイヤーのクラス定義
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([player_size, player_size])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    def update(self):
        # プレイヤーが画面外に出ないように制限
        self.rect.x = max(0, min(self.rect.x, SCREEN_WIDTH - self.rect.width))
        self.rect.y = max(0, min(self.rect.y, SCREEN_HEIGHT - self.rect.height))

# 敵クラスの定義 
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([enemy_size, enemy_size])
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - enemy_size)
        self.rect.y = random.randint(-SCREEN_HEIGHT, -enemy_size)

    def update(self):
        self.rect.y += enemy_speed
        if self.rect.y > SCREEN_HEIGHT:
            self.kill()

# スプライトグループの作成
all_sprites = pygame.sprite.Group()
enemy_sprites = pygame.sprite.Group()

# プレイヤーのスプライトインスタンスを作成し、グループに追加
player = Player()
all_sprites.add(player)

# ゲームメインプログラム
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if game_over and event.key == pygame.K_r:
                # ゲームをリスタート
                player.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
                score = 0
                player_life = 3
                game_over = False
                enemy_sprites.empty()
                all_sprites.empty()
                all_sprites.add(player)
                current_attack_cooldown = 0 # クールダウンもリセット
                current_attack_duration = 0
            
            #攻撃キー入力の追加
            if not game_over and event.key == pygame.K_SPACE and current_attack_cooldown == 0:
                current_attack_duration = attack_duration # 攻撃持続時間セット
                current_attack_cooldown = player_attack_cooldown # クールダウンセット

    if not game_over:
        # キー入力の処理
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.rect.x -= player_speed
        if keys[pygame.K_RIGHT]:
            player.rect.x += player_speed
        if keys[pygame.K_UP]:
            player.rect.y -= player_speed
        if keys[pygame.K_DOWN]:
            player.rect.y += player_speed

        player.update()

        # 敵を生成する
        spawn_counter += 1
        if spawn_counter >= ENEMY_SPAWN_INTERVAL and len(enemy_sprites) < MAX_ENEMIES:
            enemy = Enemy()
            all_sprites.add(enemy)
            enemy_sprites.add(enemy)
            spawn_counter = 0

        # 敵の更新
        enemy_sprites.update()

        # 衝突判定 (プレイヤーと敵 - 敵からダメージを受ける)
        collided_enemies_with_player = pygame.sprite.spritecollide(player, enemy_sprites, True)
        for enemy in collided_enemies_with_player:
            player_life -= 1
            if player_life <= 0:
                game_over = True

        # 画面外に出た敵はスコア加算
        for enemy in list(enemy_sprites):
            if enemy.rect.top > SCREEN_HEIGHT:
                score += 10
                enemy.kill()

        #攻撃処理
        if current_attack_cooldown > 0:
            current_attack_cooldown -= 1 # クールダウン減少

        if current_attack_duration > 0:
            current_attack_duration -= 1 # 攻撃持続時間減少

            # 攻撃判定のRectを作成 (今回はプレイヤーの右側に少し大きめに設定)
            attack_rect_width = player_size * 2
            attack_rect_height = player_size * 2
            attack_rect = pygame.Rect(
                player.rect.right - 10, # プレイヤーの右側から少しはみ出すように
                player.rect.centery - attack_rect_height // 2,
                attack_rect_width,
                attack_rect_height
            )

            # 攻撃範囲と敵の衝突判定
            # 攻撃と各敵の衝突をチェック
            # 衝突した敵を格納するリスト
            hit_enemies = []
            for enemy in enemy_sprites: 
                if attack_rect.colliderect(enemy.rect): 
                    hit_enemies.append(enemy)

            # 衝突した敵を処理
            for enemy in hit_enemies:
                enemy.kill() # 衝突した敵をグループから削除
                score += 50 # 敵を倒したらスコア加算

    # 画面の描画
    screen.fill(BLACK)

    # スコアと残機の表示
    score_text = font.render(f"Score: {score}", True, WHITE)
    life_text = font.render(f"Life: {player_life}", True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(life_text, (10, 50))

    all_sprites.draw(screen)

    #攻撃範囲の描画
    if current_attack_duration > 0:
        # 攻撃範囲を緑で描画 
        attack_rect_width = player_size * 1.5
        attack_rect_height = player_size * 1.5
        attack_rect_display = pygame.Rect(
            player.rect.right - 10,
            player.rect.centery - attack_rect_height // 2,
            attack_rect_width,
            attack_rect_height
        )
        pygame.draw.rect(screen, GREEN, attack_rect_display, 3) 

    # ゲームオーバー表示
    if game_over:
        game_over_text = font.render("GAME OVER", True, WHITE)
        restart_text = font.render("Press R to Restart", True, WHITE)
        text_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 30))
        restart_rect = restart_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 30))
        screen.blit(game_over_text, text_rect)
        screen.blit(restart_text, restart_rect)

    # 画面を更新
    pygame.display.flip()

    # フレームレートの制御
    clock.tick(60)

# Pygameの終了
pygame.quit()