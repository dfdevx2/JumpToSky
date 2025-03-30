import pygame

print("Setup Start")
pygame.init()
window = pygame.display.set_mode(size=(1560, 720))
print("Setup end")

print("Loop start")
while True:
    # check for all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # close window
            quit() # end pygame



