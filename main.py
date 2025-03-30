import pygame
from menu import Menu
from settings import WIDTH, HEIGHT

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    menu = Menu(screen)
    menu.run()

if __name__ == "__main__":
    main()
