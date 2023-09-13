import pygame 
from pygame.locals import * 
from sys import exit 

image_bg = 'closet.png'
mouse = 'gloss.png'

pygame.init()

screen = pygame.display.set_mode((640,480), 0, 32)
pygame.display.set_caption("hi")

closet = pygame.image.load(image_bg).convert()
gloss_cursor = pygame.image.load(mouse).convert()
gloss_cursor = pygame.transform.scale(gloss_cursor, (20,20)).convert()

while True:
    for event in  pygame.event.get():
        if event.type == quit:
            pygame.quit()
            exit()
        screen.blit(closet, (0,0))
        pygame.display.update()

        x = 30
        y = 70

        width = 20
        height = 20

        x, y = pygame.mouse.get_pos()     
        x -= gloss_cursor.get_height() / 2
        y -= gloss_cursor.get_height() / 2
        screen.blit(gloss_cursor, (x, y))
        
        pygame.display.update()
        

                
