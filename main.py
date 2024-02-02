import pygame
import sys
from block import Block     # Blockクラスをインポート
from paddle import Paddle   # Paddleクラスをインポート

pygame.init()

# ゲーム画面の幅と高さ
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# 色の定義（RGB
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("ブロック崩しゲーム")

# すべてのスプライトを管理するグループを作成
all_sprites = pygame.sprite.Group()

# ブロックを生成し画面の上25%に敷き詰める
def create_blocks():
    block_width = 25
    block_height = 25

    # 画面上部の25%の高さを計算
    top_height = SCREEN_HEIGHT // 4

    # ブロックを均等に配置
    for x in range(0, SCREEN_WIDTH, block_width):
        for y in range(0, top_height, block_height):
            block = Block(WHITE, block_width, block_height)
            block.rect.x = x    # ブロック位置x
            block.rect.y = y    # ブロック位置y
            all_sprites.add(block)

# パドルを生成する関数
def create_paddle():
    paddle_width = 100
    paddle_height = 20

    paddle = Paddle(WHITE, paddle_width, paddle_height)
    paddle.rect.x = (SCREEN_WIDTH - paddle_width)//2    # パドル位置x
    paddle.rect.y = SCREEN_HEIGHT - paddle_height - 10  # パドル位置y
    all_sprites.add(paddle)
    return paddle

def main():
    running = True

    create_blocks()  # ブロックを生成
    paddle = create_paddle() # パドルを生成

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # キーボード入力を処理
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            # パドルの左端が画面の左端より左にいかないように制限
            if paddle.rect.left > 0:
                paddle.move_left()
        if keys[pygame.K_RIGHT]:
            # パドルの右端が画面の右端より右に行かないように制限
            if paddle.rect.right < SCREEN_WIDTH:
                paddle.move_right()

        screen.fill(BLACK)
        
        # すべてのスプライトを描画
        all_sprites.draw(screen)
        pygame.display.flip()
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()