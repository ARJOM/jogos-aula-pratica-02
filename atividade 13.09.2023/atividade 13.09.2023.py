import pygame
from pygame.locals import *
import sys

pygame.init()

imagem_bg = 'taylor.jpeg'

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("atividade")

background = pygame.image.load(imagem_bg).convert()
background = pygame.transform.scale(background,(800,600))

tokenf = 'mirror_ball.jpeg'
token = pygame.image.load(tokenf).convert_alpha()
token = pygame.transform.scale(token, (100, 100))

white = (39, 39, 39)
blue = (0, 0, 255)

x, y = width // 2, height // 2
speed = 1

is_fullScreen = False

if __name__ == "__main__":
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            is_fullScreen = not is_fullScreen
            if is_fullScreen:
                 screen = pygame.display.set_mode((width, height), FULLSCREEN)   
            else:
                 screen = pygame.display.set_mode((width, height))    

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            x -= speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            x += speed
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            y -= speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            y += speed

        screen.blit(background, (0, 0))

        screen.blit(token, (x, y))

        pygame.display.flip()
