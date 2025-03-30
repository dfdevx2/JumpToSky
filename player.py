import pygame
from settings import GRAVITY, JUMP_STRENGTH

class Player(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.image = pygame.image.load("assets/player.png").convert_alpha()  # Carregar sprite do player
        self.rect = self.image.get_rect()
        self.rect.center = (400, 500)
        self.vel_y = 0  # Velocidade do movimento vertical (gravidade)
        self.on_ground = False
        self.game_over = False

    def update(self):
        """Atualiza o player (movimento e física)"""
        self.vel_y += GRAVITY  # Aplicando gravidade

        # Atualizando a posição vertical
        self.rect.y += self.vel_y

        # Verifica se o player está colidindo com o chão ou plataformas
        if self.rect.bottom >= self.game.screen.get_height():
            self.rect.bottom = self.game.screen.get_height()
            self.vel_y = 0
            self.on_ground = True

        # Verifica se o player colidiu com plataformas
        self.game.check_collisions()

    def jump(self):
        """Faz o player pular"""
        if self.on_ground:  # O player pode pular apenas quando estiver no chão
            self.vel_y = -JUMP_STRENGTH
            self.on_ground = False
