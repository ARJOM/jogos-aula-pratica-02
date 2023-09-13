import pygame
import sys
from pygame.locals import *

imagem_bg = 'sky.jpeg'
pygame.init()

width, height = 640,480
tela = pygame.display.set_mode((640,480), 0, 32)
tela = pygame.display.set_mode((width, height))
pygame.display.set_caption("Movimentação com Pygame")

background = pygame.image.load(imagem_bg)
background = pygame.transform.scale(background, (640, 480))

mouse = 'mario.jpeg'
token = pygame.image.load(mouse).convert_alpha()
token = pygame.transform.scale(token, (70, 70))

white = (255, 255, 255)
blue = (0, 0, 255)

x, y = width // 2, height // 2
speed = 1
is_fullscreen = False

if __name__ == "__main__":
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            tela.blit(background, (0,0))
            pygame.display.update()
               
        keys = pygame.key.get_pressed()
        if keys[pygame.K_f]:
            is_fullscreen = not is_fullscreen
            if is_fullscreen:
                tela = pygame.display\
                    .set_mode((width, height), FULLSCREEN)
            else:
                tela = pygame.display.set_mode((width, height), 0)


        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            x -= speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            x += speed
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            y -= speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            y += speed

        
        
        tela.blit(background, (0,0))

        tela.blit(token, (x, y))

        pygame.display.flip()
        
