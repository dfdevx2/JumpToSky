import pygame
from settings import GRAVITY, JUMP_STRENGTH

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("assets/player.png").convert_alpha()
        self.rect = self.image.get_rect(midbottom=(x, y))
        self.vel_y = 0

    def jump(self):
        self.vel_y = JUMP_STRENGTH

    def update(self):
        self.vel_y += GRAVITY
        self.rect.y += self.vel_y

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
