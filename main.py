import pygame
from pygame.locals import *

pygame.init()

Background = 'CÉU.jpg'
zekrom = 'ZEKROM.png'


comprimento, altura = 800,640

screen = pygame.display.set_mode((comprimento,altura))
pygame.display.set_caption('Interface')

BG = pygame.image.load(Background).convert_alpha()
token = pygame.image.load(zekrom).convert_alpha()
token = pygame.transform.scale(token,(100,100))

screen.blit(BG,(0,0))

x,y = comprimento//2, altura//2
speed = 0.5

var_control = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
    
    if event.type == VIDEORESIZE:
         screen_size = event.size
         screen = pygame.display.set_mode() 
         
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_f]:
        var_control = not var_control
        if var_control:
            screen = pygame.display.set_mode((comprimento,altura),FULLSCREEN)
        else:
            screen = pygame.display.set_mode((comprimento,altura))
            
    
    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed
        
    screen.blit(BG,(0,0))     
    screen.blit(token, (x,y))     
         
    pygame.display.update()
