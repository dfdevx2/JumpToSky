import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.image = pygame.image.load("assets/player.png").convert_alpha()
        self.rect = self.image.get_rect(midbottom=(400, 550))
        self.velocity_y = 0
        self.gravity = 0.5
        self.jump_strength = -12
        self.game = game

        # Som do pulo
        self.jump_sound = pygame.mixer.Sound("assets/player_jump.wav")

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] or keys[pygame.K_UP]:
            if self.velocity_y == 0:  # Somente pula se estiver sobre uma plataforma
                self.velocity_y = self.jump_strength
                self.jump_sound.play()

        self.velocity_y += self.gravity
        self.rect.y += self.velocity_y
