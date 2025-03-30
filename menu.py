import pygame
from settings import WIDTH, HEIGHT
from game import Game

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 40)
        self.options = ["Start Game", "Difficulty", "Score", "Exit"]
        self.selected = 0

        # Carregar as camadas do fundo do menu
        self.backgrounds = [
            pygame.image.load(f"assets/bg_menu_layer{i}.png").convert()
            for i in range(1, 7)
        ]

    def draw(self):
        self.screen.fill((0, 0, 0))

        # Desenhar camadas do fundo
        for bg in self.backgrounds:
            self.screen.blit(bg, (0, 0))

        # Desenhar opções do menu
        for i, option in enumerate(self.options):
            color = (255, 255, 255) if i == self.selected else (150, 150, 150)
            text = self.font.render(option, True, color)
            self.screen.blit(text, (WIDTH // 2 - 50, 200 + i * 50))

        pygame.display.flip()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.selected = (self.selected - 1) % len(self.options)
                    if event.key == pygame.K_DOWN:
                        self.selected = (self.selected + 1) % len(self.options)
                    if event.key == pygame.K_RETURN:
                        if self.options[self.selected] == "Start Game":
                            game = Game()
                            game.run()
                        elif self.options[self.selected] == "Exit":
                            running = False
            self.draw()
