import pygame, random, time
from settings import WIDTH, HEIGHT, FPS
from player import Player
from platform import Platform
from score_manager import ScoreManager

class Game:
    def __init__(self, difficulty):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Jump To Sky")
        self.clock = pygame.time.Clock()
        self.running = True
        self.bg = pygame.transform.scale(pygame.image.load("assets/background.png").convert(), (WIDTH, HEIGHT))
        pygame.mixer.music.load("assets/bg_music.wav")
        pygame.mixer.music.play(-1)

        self.all_sprites = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()

        self.player = Player(self, difficulty)
        self.all_sprites.add(self.player)

        # Piso inicial permanente
        self.floor = Platform(0, HEIGHT - 40)
        self.floor.image = pygame.transform.scale(pygame.image.load("assets/background.png"), (WIDTH, 40))
        self.floor.rect = self.floor.image.get_rect(topleft=(0, HEIGHT - 40))
        self.all_sprites.add(self.floor)
        self.platforms.add(self.floor)

        self.score = 0
        self.difficulty = difficulty
        self.create_platforms()

        self.start_time = time.time()
        self.score_manager = ScoreManager()
        self.font = pygame.font.Font(None, 32)

    def create_platforms(self):
        for i in range(7):
            p = Platform(random.randint(0, WIDTH-200), HEIGHT - i*100 - 100)
            self.all_sprites.add(p)
            self.platforms.add(p)

    def move_world(self, dy):
        for sprite in self.all_sprites:
            sprite.rect.y += dy
            if sprite.rect.top > HEIGHT and sprite != self.floor:
                sprite.kill()

        while len(self.platforms) < 10:
            self.create_new_platform()

        self.score = len([p for p in self.platforms if p.rect.bottom < self.player.rect.top])

    def create_new_platform(self):
        highest_platform = min(self.platforms, key=lambda p: p.rect.top)
        new_y = highest_platform.rect.top - random.randint(80, 120)
        new_x = random.randint(50, WIDTH - 200)
        new_platform = Platform(new_x, new_y)
        self.platforms.add(new_platform)
        self.all_sprites.add(new_platform)

    def save_score_menu(self, platforms_done, elapsed_time):
        name = ""
        entering_name = True
        input_rect = pygame.Rect(WIDTH//2 - 100, HEIGHT//2, 200, 32)

        while entering_name:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        entering_name = False
                    elif event.key == pygame.K_BACKSPACE:
                        name = name[:-1]
                    else:
                        if len(name) < 10:
                            name += event.unicode

            self.screen.fill((0, 0, 0))
            prompt = self.font.render("Enter your name:", True, (255, 255, 255))
            input_surface = self.font.render(name, True, (255, 255, 255))
            self.screen.blit(prompt, (WIDTH//2 - prompt.get_width()//2, HEIGHT//2 - 40))
            pygame.draw.rect(self.screen, (255, 255, 255), input_rect, 2)
            self.screen.blit(input_surface, (input_rect.x+5, input_rect.y+5))
            pygame.display.flip()
            self.clock.tick(30)

        self.score_manager.add_score(name, platforms_done, elapsed_time)

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.running = False  # Retorna ao menu principal

            self.all_sprites.update()

            if self.player.rect.top > HEIGHT or self.score >= 150:
                self.running = False

            self.screen.blit(self.bg, (0, 0))
            self.all_sprites.draw(self.screen)

            # Temporizador e contador de plataformas
            elapsed_time = time.time() - self.start_time
            minutes = int(elapsed_time // 60)
            seconds = int(elapsed_time % 60)

            time_text = self.font.render(f"Time: {minutes:02}:{seconds:02}", True, (255, 255, 255))
            platforms_done = len([p for p in self.platforms if p.rect.bottom < self.player.rect.top])
            remaining = 150 - platforms_done
            platform_text = self.font.render(f"Platforms: {platforms_done}/150 (Remaining: {remaining})", True, (255, 255, 255))

            self.screen.blit(time_text, (10, 10))
            self.screen.blit(platform_text, (10, 40))

            pygame.display.flip()
            self.clock.tick(FPS)

        pygame.mixer.music.stop()

        # Salvar pontuação (se tiver jogado)
        if platforms_done > 0:
            self.save_score_menu(platforms_done, elapsed_time)

        # Automaticamente retorna ao menu principal aqui
