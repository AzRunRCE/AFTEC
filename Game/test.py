import pygame
from pygame.locals import *
pygame.init()
#Listes des images du jeu
caract_down = "perso_down.png"
caract_up = "perso_up.png"
caract_left = "perso_left.png"
caract_rigth = "perso_rigth.png"
fenetre = pygame.display.set_mode((640, 480))
fond = pygame.image.load("background.jpg").convert()
fenetre.blit(fond, (0,0))
animation = pygame.image.load("sprite.png").convert()
x, y, WIDTH, HEIGHT = 2, 12, 20, 30
pygame.time.Clock().tick(30)
perso = pygame.image.load(caract_down).convert_alpha()
position_perso = perso.get_rect()
fenetre.blit(perso, (320,240))
pygame.display.flip()
pygame.key.set_repeat(100, 30)
sprite = animation.get_rect(x=x*WIDTH, y=y, w=WIDTH, h=HEIGHT)
#BOUCLE INFINIE
continuer = 1
while continuer:
    for event in pygame.event.get():	
        if event.type == QUIT:
            print(x,y,WIDTH,HEIGHT)
            continuer = 0
        if event.type == KEYDOWN:
            if event.key == K_DOWN:       
                y = y -1
            if event.key == K_UP:       
                y = y +1  
            if event.key == K_LEFT:    
                x = x +1     
            if event.key == K_RIGHT:       
                x = x -1     
               
	sprite = animation.get_rect(x=x, y=y, w=WIDTH, h=HEIGHT)
    #Re-collage
    fenetre.blit(fond, (0,0))	
    fenetre.blit(animation, (10, 10), sprite)
    #Rafraichissement
    pygame.display.flip()
