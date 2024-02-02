import pygame
import cv2
import sys
from block import Block     # Blockクラスをインポート
from paddle import Paddle   # Paddleクラスをインポート
from ball import Ball       # Ballクラスをインポート

pygame.init()

# ゲーム画面の幅と高さ
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# 色の定義（RGB
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# ゲームループのフレームレートを設定
FPS = 30
clock = pygame.time.Clock()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("ブロック崩しゲーム")

# すべてのスプライトを管理するグループを作成
all_sprites = pygame.sprite.Group()
blocks_group = pygame.sprite.Group()

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
            blocks_group.add(block)

# パドルを生成する関数
def create_paddle():
    paddle_width = 100
    paddle_height = 20

    paddle = Paddle(WHITE, paddle_width, paddle_height)
    paddle.rect.x = (SCREEN_WIDTH - paddle_width)//2    # パドル位置x
    paddle.rect.y = SCREEN_HEIGHT - paddle_height - 10  # パドル位置y
    all_sprites.add(paddle)
    return paddle

# ボールを生成する関数
def create_ball(color, size, init_pos_x, init_pos_y, blocks_group):
    ball = Ball(color, size, blocks_group)
    ball.rect.x = init_pos_x
    ball.rect.y = init_pos_y
    ball.speed = [5, 5]
    all_sprites.add(ball)
    return ball

# 動画を記録する関数（今はうまく行っていない、そもそもゲームが遅くなるのでやらないほうが良さそう）
def save_video(frames, width, height):
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('gameplay.avi', fourcc, 30.0, (width, height))
    for frame in frames:
        out.write(cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
    out.release()

def main():
    running = True
    recording = False   # 録画中かどうかを示すフラグ
    frames = []         # フレームを格納するリスト

    create_blocks()                 # ブロックを生成
    paddle = create_paddle()        # パドルを生成
    ball = create_ball(WHITE, 10, SCREEN_WIDTH//2, SCREEN_HEIGHT//2, blocks_group)   # ボールを生成

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # # スペースキーが押された場合に録画を停止してビデオファイルに保存
            # if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            #     if recording:
            #         recording = False
            #         save_video(frames, SCREEN_WIDTH, SCREEN_HEIGHT)
            #         frames = []     # フレームリストをリセット
            #     else:
            #         recording = True

        # Enterキーが押下されたらボールをリセット
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            # ボールを消去
            all_sprites.remove(ball)
            ball.kill()
            # ボール再生成
            ball = create_ball(WHITE, 10, SCREEN_WIDTH//2, SCREEN_HEIGHT//2, blocks_group)

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

        # ボール位置を更新
        ball.update(paddle, SCREEN_WIDTH, SCREEN_HEIGHT)

        screen.fill(BLACK)
        
        # すべてのスプライトを描画
        all_sprites.draw(screen)
        pygame.display.flip()

        # # 録画中の場合、ゲーム画面をキャプチャしてフレームリストに追加
        # if recording:
        #     frame = pygame.surfarray.array3d(screen)
        #     frames.append(frame)

        # フレームレートを制御
        clock.tick(FPS)
            
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()