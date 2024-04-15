import pygame, sys  

pygame.init()
DISPLAYSURF = pygame.display.set_mode((200, 50))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()