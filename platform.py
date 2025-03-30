import pygame
from settings import PLATFORM_WIDTH, PLATFORM_HEIGHT

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((PLATFORM_WIDTH * 2, PLATFORM_HEIGHT))  # Criar plataforma dupla
        texture = pygame.image.load("assets/platform.png").convert_alpha()
        self.image.blit(texture, (0, 0))  # Primeira parte da plataforma
        self.image.blit(texture, (PLATFORM_WIDTH, 0))  # Segunda parte ao lado
        self.rect = self.image.get_rect(topleft=(x, y))
