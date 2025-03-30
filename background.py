import pygame


class Background:
    def __init__(self):
        self.layers = [
            pygame.image.load(f"assets/bg_layer{i}.png").convert() for i in range(1, 7)
        ]
        self.y_offset = 0

    def update(self, player_y):
        self.y_offset = -player_y * 0.2

    def draw(self, screen):
        for i, layer in enumerate(self.layers):
            screen.blit(layer, (0, self.y_offset * (i + 1)))