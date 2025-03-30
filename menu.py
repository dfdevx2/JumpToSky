# menu.py
import pygame
import os
from settings import WIDTH, HEIGHT  # Certifique-se de ter essas variáveis no settings.py


class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 48)

        # Carregar as 6 camadas do background
        self.bg_layers = [
            pygame.image.load(os.path.join("assets", "bg_menu_layer1.png")).convert(),
            pygame.image.load(os.path.join("assets", "bg_menu_layer2.png")).convert(),
            pygame.image.load(os.path.join("assets", "bg_menu_layer3.png")).convert(),
            pygame.image.load(os.path.join("assets", "bg_menu_layer4.png")).convert(),
            pygame.image.load(os.path.join("assets", "bg_menu_layer5.png")).convert(),
            pygame.image.load(os.path.join("assets", "bg_menu_layer6.png")).convert()
        ]

        # Ajustando a escala das camadas para caber na tela
        self.bg_layers = [pygame.transform.scale(layer, (WIDTH, HEIGHT)) for layer in self.bg_layers]

        # Definindo as opções do menu
        self.menu_items = ["Start Game", "Difficulty", "Score", "Exit"]
        self.selected_item = 0
        self.difficulty = "Normal"  # A dificuldade inicial
        self.in_difficulty_menu = False  # Variável para controlar o submenu de dificuldade

    def update_background(self, player_y):
        """Atualiza o fundo com as camadas se movendo com o jogador."""
        for i, layer in enumerate(self.bg_layers):
            offset = (player_y // (i + 1))  # Distância variável para a camada
            self.screen.blit(layer, (0, offset))

    def draw(self):
        """Desenha todos os elementos do menu, incluindo o fundo e os itens do menu."""
        self.update_background(0)  # A princípio, o player_y é 0 para o menu

        # Desenha os itens do menu
        for i, item in enumerate(self.menu_items):
            color = (255, 0, 0) if i == self.selected_item else (255, 255, 255)
            label = self.font.render(item, True, color)
            self.screen.blit(label, (WIDTH // 2 - label.get_width() // 2, 200 + i * 60))

        # Se estiver no submenu de "Difficulty", mostra as opções
        if self.in_difficulty_menu:
            difficulty_font = pygame.font.Font(None, 36)
            difficulty_options = ["Easy", "Normal", "Hard"]
            for i, option in enumerate(difficulty_options):
                color = (255, 0, 0) if option == self.difficulty else (255, 255, 255)
                label = difficulty_font.render(option, True, color)
                self.screen.blit(label, (WIDTH // 2 - label.get_width() // 2, 300 + i * 60))

    def update(self):
        """Atualiza os botões e checa as interações."""
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()

        # Detecta o clique do mouse
        for i, item in enumerate(self.menu_items):
            label = self.font.render(item, True, (255, 0, 0 if i == self.selected_item else 255))
            rect = pygame.Rect(WIDTH // 2 - label.get_width() // 2, 200 + i * 60, label.get_width(), label.get_height())
            if rect.collidepoint(mouse_pos) and mouse_pressed[0]:
                if i == 0:
                    return "start_game"
                elif i == 1:
                    return "difficulty"
                elif i == 2:
                    return "score"
                elif i == 3:
                    return "exit"

        return None

    def navigate_difficulty(self):
        """Navega pelas opções de dificuldade se a opção estiver selecionada."""
        if self.in_difficulty_menu:  # Se estiver no submenu de "Difficulty"
            difficulty_options = ["Easy", "Normal", "Hard"]
            self.difficulty = difficulty_options[(difficulty_options.index(self.difficulty) + 1) % 3]
            print(f"Difficulty set to: {self.difficulty}")
            return "difficulty_selected"

        return None

    def run(self):
        """Executa o loop do menu."""
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and not self.in_difficulty_menu and self.selected_item > 0:
                        self.selected_item -= 1
                    elif event.key == pygame.K_DOWN and not self.in_difficulty_menu and self.selected_item < len(
                            self.menu_items) - 1:
                        self.selected_item += 1
                    elif event.key == pygame.K_RETURN:
                        action = self.update()
                        if action == "start_game":
                            print("Start Game clicked!")
                            return "start_game"
                        elif action == "difficulty":
                            print("Difficulty clicked!")
                            self.in_difficulty_menu = True  # Abre o submenu de Difficulty
                        elif action == "score":
                            print("Score clicked!")
                            return "score"
                        elif action == "exit":
                            print("Exit clicked!")
                            pygame.quit()
                            exit()
                    elif event.key == pygame.K_ESCAPE:
                        if self.in_difficulty_menu:
                            self.in_difficulty_menu = False  # Fecha o submenu de Difficulty
                        else:
                            running = False  # Sai do loop e fecha o jogo

                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    action = self.update()
                    if action:
                        if action == "start_game":
                            return "start_game"
                        elif action == "difficulty":
                            self.in_difficulty_menu = True  # Abre o submenu de Difficulty
                        elif action == "score":
                            return "score"
                        elif action == "exit":
                            pygame.quit()
                            exit()

            self.screen.fill((0, 0, 0))  # Limpa a tela
            self.draw()  # Desenha o menu
            pygame.display.flip()
            self.clock.tick(60)  # Controla o FPS

        pygame.quit()
