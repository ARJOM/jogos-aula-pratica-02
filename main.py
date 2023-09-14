import pygame
from pygame.locals import *
import sys

pygame.init()

largura, altura = 800, 600
screen = pygame.display.set_mode((largura, altura), FULLSCREEN)
pygame.display.set_caption("Aula-Pratica-Jogos-Digitais")

player = 'assets/luffytaro.png'
background = 'assets/desktop-wallpaper-steam-community-8-bit-purple-sunset-eight-bit-sunset.jpg'

token = pygame.image.load(player).convert_alpha()
token = pygame.transform.scale(token, (50, 50))
tela = pygame.image.load(background).convert_alpha()
tela = pygame.transform.scale(tela, (largura, altura))

white = (255, 255, 255)
blue = (0, 0, 255)
tc_screen = False
x, y = largura // 2, altura // 2
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
                screen = pygame.display.set_mode((largura, altura), FULLSCREEN)
            else:
                screen = pygame.display.set_mode((largura, altura))

        screen.blit(tela, (0, 0))
        screen.blit(token, (x, y))

        pygame.display.flip()
