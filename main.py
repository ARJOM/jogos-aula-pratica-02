
import pygame
from pygame.locals import *
import sys
import time

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("meu mundo!")

bg = 'fundo.png'
bg1 = pygame.image.load(bg).convert()
bg1 = pygame.transform.scale(bg1, (800, 600))

player = 'jogadora.png'
player1 = pygame.image.load(player).convert_alpha()
player1 = pygame.transform.scale(player1, (160, 160))

is_fullscreen = False

x, y = 350, 400

speed = 0.5

if __name__ == "__main__":
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        
        
        if keys[pygame.K_f]:
          is_fullscreen = not is_fullscreen
          if is_fullscreen:
              screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
          else:
              screen = pygame.display.set_mode((width, height), 0)
        
        if keys[pygame.K_LEFT]:
            x -= speed
        if keys[pygame.K_RIGHT]:
            x += speed
        if keys[pygame.K_UP]:
            y -= speed
        if keys[pygame.K_DOWN]:
            y += speed
        
        
        screen.blit(bg1, (0, 0))
        screen.blit(player1, (x, y))
        
        pygame.display.flip()
