import pygame
from pygame.locals import * 
import sys

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height), FULLSCREEN)
pygame.display.set_caption("Movimentação com Pygame")

image_bg = 'closet.png'
mouse = 'gloss.png'

token = pygame.image.load(mouse).convert_alpha()
token = pygame.transform.scale(token, (20, 20))
closet = pygame.image.load(image_bg).convert()
closet = pygame.transform.scale(closet, (width, height))
is_fullscreen = False
x, y = width // 2, height // 2
speed = 0.5

if __name__ == "__main__":
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            x -= speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            x += speed
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            y -= speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            y += speed
        if keys[pygame.K_f]:
            is_fullscreen = not is_fullscreen 
            if is_fullscreen:
                screen = pygame.display.set_mode((width, height), FULLSCREEN)
            else:
                screen = pygame.display.set_mode((width, height), 0)

        screen.blit(closet, (0,0))
        screen.blit(token, (x, y))

        pygame.display.flip()