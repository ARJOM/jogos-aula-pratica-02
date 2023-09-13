import pygame
from pygame.locals import *
import sys

pygame.init()

larg, altu = 800, 600
screen = pygame.display.set_mode((larg, altu), FULLSCREEN)
pygame.display.set_caption("Movimentação com Pygame")

mouse = 'assets/cursor_swordman.png'
image_bg = 'assets/image_background.jpg'

token = pygame.image.load(mouse).convert_alpha()
token = pygame.transform.scale(token, (50, 50))
background = pygame.image.load(image_bg).convert_alpha()
background = pygame.transform.scale(background, (larg, altu))

white = (255, 255, 255)
blue = (0, 0, 255)
tc_screen = False
x, y = larg // 2, altu // 2
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
            tc_screen = not tc_screen
            if tc_screen:
                screen = pygame.display.set_mode((larg, altu), FULLSCREEN)
            else:
                screen = pygame.display.set_mode((larg, altu))

        screen.blit(background, (0, 0))
        screen.blit(token, (x, y))

        pygame.display.flip()