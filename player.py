import pygame
from settings import WIDTH, HEIGHT

class Player(pygame.sprite.Sprite):
    def __init__(self, game, difficulty):
        super().__init__()
        self.game = game
        self.image = pygame.image.load("assets/player.png").convert_alpha()
        self.rect = self.image.get_rect(midbottom=(WIDTH // 2, HEIGHT - 120))

        # Configurações de dificuldade
        if difficulty == "Easy":
            self.speed = 5
            self.gravity = 0.4
            self.jump_strength = -13
        elif difficulty == "Hard":
            self.speed = 7
            self.gravity = 0.7
            self.jump_strength = -11
        else:  # Normal
            self.speed = 5
            self.gravity = 0.5
            self.jump_strength = -12

        self.vel_y = 0
        self.on_ground = False
        self.current_platform = None
        self.jump_sound = pygame.mixer.Sound("assets/player_jump.wav")

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if (keys[pygame.K_SPACE] or keys[pygame.K_UP]) and self.on_ground:
            self.vel_y = self.jump_strength
            self.jump_sound.play()
            self.on_ground = False
            if self.current_platform and self.current_platform != self.game.floor:
                self.current_platform.kill()
                self.current_platform = None

        self.rect.left = max(0, self.rect.left)
        self.rect.right = min(WIDTH, self.rect.right)

        self.vel_y += self.gravity
        self.rect.y += self.vel_y

        if self.rect.top <= HEIGHT // 3:
            self.game.move_world(abs(self.vel_y))

        if self.rect.top > HEIGHT:
            self.game.running = False

        self.check_collisions()

    def check_collisions(self):
        self.on_ground = False
        hits = pygame.sprite.spritecollide(self, self.game.platforms, False)
        if hits and self.vel_y > 0:
            platform = hits[0]
            self.rect.bottom = platform.rect.top
            self.vel_y = 0
            self.on_ground = True
            self.current_platform = platform
