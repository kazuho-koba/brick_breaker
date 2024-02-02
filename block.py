import pygame

# ブロックのクラスを定義
class Block(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()

        # ブロックの外観を設定
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()