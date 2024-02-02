import pygame

class Ball(pygame.sprite.Sprite):
    def __init__(self, color, radius, blocks_group):
        super().__init__()

        self.image = pygame.Surface([2*radius, 2*radius], pygame.SRCALPHA)
        pygame.draw.circle(self.image, color, (radius, radius), radius)
        self.rect = self.image.get_rect()

        self.radius = radius
        self.speed = [0, 0]     # ボールの速度(x,y)
        self.blocks_group = blocks_group

    def update(self, paddle, SCREEN_WIDTH, SCREEN_HEIGHT):
        self.rect.x += self.speed[0]
        self.rect.y += self.speed[1]
        # print(self.speed)

        # パドルとの衝突検出
        if pygame.sprite.collide_rect(self, paddle):
            # パドルに当たった場合の処理
            self.speed[1] = -self.speed[1]  # y方向の速度を反転

        # 画面端での反射
        if self.rect.left <= 0 or self.rect.right >= SCREEN_WIDTH:
            self.speed[0] = -self.speed[0]
        if self.rect.top <= 0:
            self.speed[1] = -self.speed[1]

        # print(self.rect.top)

        # ブロックとの衝突検出
        block_hits = pygame.sprite.spritecollide(self, self.blocks_group, True)
        if block_hits:
            block = block_hits[0]
            block.leftedge = block.rect.x
            block.rightedge = block.rect.x + block.rect.width

            # ボールがブロックの側面にぶつかった場合はx方向速度を反転
            if self.rect.right <= block.leftedge or self.rect.left >= block.rightedge:
                self.speed[0] = -self.speed[0]
            else:
                self.speed[1] = -self.speed[1]
                