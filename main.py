import pygame 
from pygame.locals import * 
from sys import exit 

img_bg = 'iohanalinda.jpeg'
mouse = 'iohana.png'

pygame.init()

tela = pygame.display.set_mode((640,480), 0, 32)
pygame.display.set_caption("OLÁ MUNDO")

background = pygame.image.load(img_bg).convert()
mouse_cursor = pygame.image.load(mouse).convert()
mouse_cursor = pygame.transform.scale(mouse_cursor, (20, 20)).convert()
background = pygame.transform.scale(background, (640, 480)).convert()
pygame.mouse.set_visible(False)
if __name__=='__main__':
    while True:
        for event in  pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        
        

            tela.blit(background, (0, 0))
            pygame.display.update()
            x, y = pygame.mouse.get_pos()
            x -= mouse_cursor.get_width() / 2
            y -= mouse_cursor.get_height() / 2
            tela.blit(mouse_cursor, (x, y))

            pygame.display.update()
        
       