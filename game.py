import pygame
import random
from settings import WIDTH, HEIGHT, FPS
from player import Player
from platform import Platform


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Jump to Sky")
        self.clock = pygame.time.Clock()

        # Carregar imagens
        self.bg = pygame.image.load("assets/background.png").convert()

        # Criar grupos de sprites
        self.all_sprites = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()

        # Criar player
        self.player = Player(self)
        self.all_sprites.add(self.player)

        # Criar piso inicial
        self.floor = Platform(WIDTH // 2 - 100, HEIGHT - 50)
        self.all_sprites.add(self.floor)
        self.platforms.add(self.floor)

        # Criar plataformas iniciais
        for i in range(5):
            x = random.randint(50, WIDTH - 200)
            y = HEIGHT - (i * 100) - 100
            platform = Platform(x, y)
            self.all_sprites.add(platform)
            self.platforms.add(platform)

    def run(self):
        running = True
        while running:
            self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.update()
            self.draw()
        pygame.quit()

    def update(self):
        self.all_sprites.update()

        # Se o player sobe, move tudo para baixo
        if self.player.rect.top < HEIGHT // 2:
            self.player.rect.y += 5
            for platform in self.platforms:
                platform.rect.y += 5
                if platform.rect.top > HEIGHT:
                    platform.kill()
                    self.create_platform()

    def draw(self):
        self.screen.blit(self.bg, (0, 0))
        self.all_sprites.draw(self.screen)
        pygame.display.flip()

    def create_platform(self):
        """Cria novas plataformas proceduralmente."""
        x = random.randint(50, WIDTH - 200)
        y = random.randint(-50, 0)
        platform = Platform(x, y)
        self.all_sprites.add(platform)
        self.platforms.add(platform)
