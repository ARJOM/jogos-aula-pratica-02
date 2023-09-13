import sys, pygame
from pygame.locals import *

screen  = pygame.display.set_mode((1280, 720), pygame.SCALED)
pygame.display.set_caption("Atividade de Jogos Digitais")
clock = pygame.time.Clock()
is_fullscreen = False

pc = pygame.image.load("Kazuma_Kiryu.png").convert_alpha()
pc = pygame.transform.scale(pc, (320, 480))
ANIM = pygame.USEREVENT + 0
is_flipped = False
pygame.time.set_timer(ANIM, 500)

bg = pygame.image.load("bg4.jpg").convert()
bg = pygame.transform.scale(bg, (1280, 720))



px, py = 0, 0
speed = 3

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit
            exit()
        if event.type == ANIM:
            if is_flipped == False:
                pc = pygame.transform.flip(pc, 1 ,0)
                is_flipped == True
            else:
                pc = pygame.transform.flip(pc, 0, 0)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_f]:
        is_fullscreen = not is_fullscreen
        if is_fullscreen:
            pygame.display.toggle_fullscreen()
        else:
            pygame.display.toggle_fullscreen()

    if keys[pygame.K_UP]:
        py -=speed
    if keys[pygame.K_DOWN]:
        py +=speed
    if keys[pygame.K_LEFT]:
        px -=speed    
    if keys[pygame.K_RIGHT]:
        px +=speed
    
    
    screen.blit(bg, (0, 0))
    screen.blit(pc, (px, py))
    clock.tick(60)

    pygame.display.flip()
