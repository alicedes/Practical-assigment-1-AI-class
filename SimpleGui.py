import pygame

pygame.init()

WINDOWSIZE=(1000,800)
PURPLE=(186,85,211)
BLACK=(0,0,0)
WHITE=(255,255,255)

running=True
screen= pygame.display.set_mode(WINDOWSIZE)
pygame.display.set_caption("4x6 Checkers")


while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False  
    screen.fill(PURPLE)
    pygame.display.update()

pygame.quit()
