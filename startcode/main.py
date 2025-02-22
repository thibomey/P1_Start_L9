import pygame, sys
from pygame.locals import QUIT

pygame.init()
venster = pygame.display.set_mode((1500 , 700))
venster.fill((255,255,255))
#color = (Color_r, 0, 0)
penseel = 8
Color_r = 0
Color_g = 0
Color_b = 0
color = (Color_r, Color_g, Color_b)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        #Pen
        if pygame.mouse.get_pressed() == (True, False, False):
            pygame.draw.circle(venster, color, pygame.mouse.get_pos(), penseel)
        #Gom
        if pygame.mouse.get_pressed() == (False, False, True):
            pygame.draw.circle(venster, (255, 255, 255), pygame.mouse.get_pos(), 50)

        #Leeg canvas
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    venster.fill((255, 255, 255))

        #Opslaan
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                filename = input("filename: ")
                pygame.image.save(venster, filename + ".jpg")

        #Scrollwheel
        if event.type == pygame.MOUSEWHEEL:
            if event.y == -1:
                penseel -= 1
            else:
                penseel += 1

        #Colors
        ''''
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                color = (255, 0, 0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z:
                color = (0, 0, 0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_b:
                color = (0, 0, 255)
        pygame.display.update()
        '''
        #IOP = RGB kleuren veranderen door toetsen
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_i:
                Color_r +=10
                if Color_r > 255:
                    Color_r = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_o:
                Color_g +=10
                if Color_g > 255:
                    Color_g = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                Color_b +=10
                if Color_b > 255:
                    Color_b = 0
        color = (Color_r, Color_g, Color_b)
    pygame.display.update()
