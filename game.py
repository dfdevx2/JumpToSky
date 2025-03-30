import pygame
import random
from player import Player
from platform import Platform
from settings import WIDTH, HEIGHT, GRAVITY


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Inicializando a tela
        self.clock = pygame.time.Clock()

        # Inicializando as camadas de fundo
        self.background_layers = [
            {"image": pygame.image.load("assets/bg_layer1.png").convert(), "speed": 0.1},
            {"image": pygame.image.load("assets/bg_layer2.png").convert(), "speed": 0.2},
            {"image": pygame.image.load("assets/bg_layer3.png").convert(), "speed": 0.3},
            {"image": pygame.image.load("assets/bg_layer4.png").convert(), "speed": 0.4},
            {"image": pygame.image.load("assets/bg_layer5.png").convert(), "speed": 0.5},
            {"image": pygame.image.load("assets/bg_layer6.png").convert(), "speed": 0.6},
        ]

        self.all_sprites = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()

        # Player
        self.player = Player(self)
        self.all_sprites.add(self.player)

        # Criar plataformas iniciais
        self.create_initial_platforms()

        # Variáveis de controle
        self.platform_count = 0
        self.game_over = False

    def create_initial_platforms(self):
        """Cria plataformas iniciais para o player começar a subir"""
        platform1 = Platform(100, 500)
        platform2 = Platform(300, 400)
        platform3 = Platform(500, 300)
        self.all_sprites.add(platform1, platform2, platform3)
        self.platforms.add(platform1, platform2, platform3)

    def move_background(self):
        """Movimenta as camadas de fundo"""
        for layer in self.background_layers:
            # Inicializando a posição da camada
            layer["rect"] = layer.get("rect", layer["image"].get_rect())
            layer["rect"].y += 1 * layer["speed"]

            # Fazendo a camada de fundo se repetir para criar o efeito contínuo
            if layer["rect"].y >= self.screen.get_height():
                layer["rect"].y = -self.screen.get_height()

            # Desenha o fundo na tela
            self.screen.blit(layer["image"], layer["rect"])

    def generate_platform(self):
        """Gera uma nova plataforma aleatória no topo da tela"""
        if random.randint(1, 100) <= 2:  # Chance de gerar nova plataforma
            x = random.randint(50, 750)
            y = random.randint(-100, -50)
            platform = Platform(x, y)
            self.all_sprites.add(platform)
            self.platforms.add(platform)
            self.platform_count += 1

    def check_collisions(self):
        """Verifica colisões do player com as plataformas"""
        if self.player.vel_y > 0:  # Apenas verifica se estiver caindo
            collisions = pygame.sprite.spritecollide(self.player, self.platforms, False)
            for platform in collisions:
                if self.player.rect.colliderect(platform.rect) and self.player.rect.bottom <= platform.rect.top + 10:
                    self.player.on_ground = True
                    self.player.vel_y = 0
                    self.player.rect.bottom = platform.rect.top
                    break
                else:
                    self.player.on_ground = False

    def handle_player_input(self):
        """Lida com a entrada do jogador (pulo)"""
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] or keys[pygame.K_SPACE]:  # Se pressionado seta para cima ou espaço
            self.player.jump()

    def run(self):
        running = True
        while running:
            self.screen.fill((0, 0, 0))  # Limpa a tela

            # Captura os eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False

            # Move o background
            self.move_background()

            # Gera novas plataformas
            self.generate_platform()

            # Lida com a entrada do jogador (pulo)
            self.handle_player_input()

            # Atualiza o player e as plataformas
            self.all_sprites.update()

            # Desenha tudo na tela
            self.all_sprites.draw(self.screen)

            # Verifica se o player atingiu o objetivo
            if self.platform_count >= 100:
                self.game_over = True
                self.show_win_screen()

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()

    def show_win_screen(self):
        """Exibe a tela de vitória"""
        font = pygame.font.SysFont('Arial', 36)
        text = font.render('Você venceu! Objetivo alcançado: 100 plataformas!', True, (255, 255, 255))
        self.screen.blit(text, (50, self.screen.get_height() // 2))
        pygame.display.flip()
        pygame.time.wait(2000)  # Exibe por 2 segundos


# Rodar o jogo
if __name__ == "__main__":
    game = Game()
    game.run()
