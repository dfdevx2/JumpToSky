import pygame
from player import Player
from platform import Platform

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Jump To Sky")
        self.clock = pygame.time.Clock()
        self.running = True

        # Música do jogo
        pygame.mixer.music.load("assets/bg_music.wav")
        pygame.mixer.music.play(-1)

        self.all_sprites = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()

        # Criar plataformas iniciais
        initial_platforms = [Platform(300, 500), Platform(400, 400), Platform(200, 300)]
        for platform in initial_platforms:
            self.all_sprites.add(platform)
            self.platforms.add(platform)

        self.player = Player(self)
        self.all_sprites.add(self.player)

    def run(self):
        while self.running:
            self.events()
            self.update()
            self.draw()
            self.clock.tick(60)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        self.all_sprites.update()

        # Verificar colisão com plataformas
        for platform in self.platforms:
            if self.player.rect.colliderect(platform.rect) and self.player.velocity_y > 0:
                self.player.rect.bottom = platform.rect.top
                self.player.velocity_y = 0
                platform.kill()  # Remove a plataforma após ser usada

    def draw(self):
        self.screen.fill((135, 206, 250))  # Fundo azul céu
        self.all_sprites.draw(self.screen)
        pygame.display.flip()
