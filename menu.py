import pygame
from settings import WIDTH, HEIGHT
from game import Game
from score_manager import ScoreManager

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 36)
        self.options = ["Start Game", "Difficulty", "Score", "Exit"]
        self.difficulties = ["Easy", "Normal", "Hard"]
        self.selected = 0
        self.selected_diff = 1
        self.state = "main"
        self.bg_layers = [pygame.transform.scale(pygame.image.load(f"assets/bg_menu_layer{i}.png").convert(), (WIDTH, HEIGHT)) for i in range(1, 7)]
        pygame.mixer.music.load("assets/bg_music.wav")
        pygame.mixer.music.play(-1)
        self.score_manager = ScoreManager()

    def draw(self):
        for bg in self.bg_layers:
            self.screen.blit(bg, (0, 0))

        options = self.options if self.state == "main" else self.difficulties if self.state == "difficulty" else ["Back"]
        selected_idx = self.selected if self.state == "main" else self.selected_diff if self.state == "difficulty" else 0

        for idx, opt in enumerate(options):
            color = (255,255,255) if idx == selected_idx else (100,100,100)
            text = self.font.render(opt, True, color)
            self.screen.blit(text, (WIDTH//2 - text.get_width()//2, 200 + idx*40))

        if self.state == "score":
            scores = self.score_manager.get_scores()[:10]  # Top 10 scores
            for idx, score in enumerate(scores):
                score_text = self.font.render(f"{score[1]}: Platforms {score[2]}, Time {int(score[3]//60)}:{int(score[3]%60):02}", True, (255,255,0))
                self.screen.blit(score_text, (WIDTH//2 - score_text.get_width()//2, 300 + idx*30))

        pygame.display.flip()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        if self.state == "main":
                            self.selected = (self.selected - 1) % len(self.options)
                        elif self.state == "difficulty":
                            self.selected_diff = (self.selected_diff - 1) % len(self.difficulties)
                    if event.key == pygame.K_DOWN:
                        if self.state == "main":
                            self.selected = (self.selected + 1) % len(self.options)
                        elif self.state == "difficulty":
                            self.selected_diff = (self.selected_diff + 1) % len(self.difficulties)
                    if event.key == pygame.K_RETURN:
                        if self.state == "main":
                            if self.options[self.selected] == "Start Game":
                                difficulty = self.difficulties[self.selected_diff]
                                game = Game(difficulty)
                                game.run()
                                pygame.mixer.music.load("assets/bg_music.wav")
                                pygame.mixer.music.play(-1)
                            elif self.options[self.selected] == "Difficulty":
                                self.state = "difficulty"
                            elif self.options[self.selected] == "Score":
                                self.state = "score"
                            elif self.options[self.selected] == "Exit":
                                running = False
                        elif self.state in ["difficulty", "score"]:
                            self.state = "main"
                    if event.key == pygame.K_ESCAPE and self.state in ["difficulty", "score"]:
                        self.state = "main"
            self.draw()
