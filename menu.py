import pygame
from game import Game

pygame.init()

class Menu:
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Jump To Sky - Menu")
        self.clock = pygame.time.Clock()
        self.running = True

        # Música de fundo
        pygame.mixer.music.load("assets/bg_music.wav")
        pygame.mixer.music.play(-1)

    def run(self):
        while self.running:
            self.screen.fill((50, 50, 50))
            font = pygame.font.Font(None, 36)
            text = font.render("Press ENTER to Start", True, (255, 255, 255))
            self.screen.blit(text, (300, 250))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        game = Game()
                        game.run()
                    if event.key == pygame.K_ESCAPE:
                        self.running = False

            self.clock.tick(60)

        pygame.quit()
