# button.py
import pygame

class Button:
    def __init__(self, screen, text, x, y, width=200, height=50):
        self.screen = screen
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.font = pygame.font.Font(None, 40)
        self.rect = pygame.Rect(x, y, width, height)
        self.color = (0, 128, 255)

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
        label = self.font.render(self.text, True, (255, 255, 255))
        self.screen.blit(label, (self.x + (self.width - label.get_width()) // 2, self.y + (self.height - label.get_height()) // 2))

        # Detecta cliques
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()
        if self.rect.collidepoint(mouse_pos) and mouse_pressed[0]:
            return True
        return False
