# platform.py
import pygame

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("assets/platform.png").convert_alpha()  # Carregar sprite da plataforma
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
