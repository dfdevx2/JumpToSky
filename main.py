# main.py
import pygame
from menu import Menu
from game import Game

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    menu = Menu(screen)

    # Loop do menu
    while True:
        action = menu.run()
        if action == "start_game":
            game = Game()
            game.run()
        elif action == "exit":
            pygame.quit()
            exit()

if __name__ == "__main__":
    main()
