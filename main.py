import pygame
from menu import Menu
from settings import WIDTH, HEIGHT

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Jump To Sky")
    menu = Menu(screen)
    menu.run()

if __name__ == "__main__":
    main()
