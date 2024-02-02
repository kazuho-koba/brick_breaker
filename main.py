import pygame
import sys
from block import Block # Blockクラスをインポート

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
def creat_blocks():
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

def main():
    running = True

    # ブロックを生成
    creat_blocks()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)
        
        # すべてのスプライトを描画
        all_sprites.draw(screen)
        pygame.display.flip()
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()