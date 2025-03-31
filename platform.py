import pygame
from settings import PLATFORM_WIDTH, PLATFORM_HEIGHT

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        block = pygame.transform.scale(pygame.image.load("assets/platform.png").convert_alpha(), (PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.image = pygame.Surface((PLATFORM_WIDTH*2, PLATFORM_HEIGHT), pygame.SRCALPHA)
        self.image.blit(block, (0, 0))
        self.image.blit(block, (PLATFORM_WIDTH, 0))
        self.rect = self.image.get_rect(topleft=(x, y))
