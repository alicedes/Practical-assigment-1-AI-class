import pygame

pygame.init()

WINDOWSIZE=(1000,800)
running=True
screen= pygame.display.set_mode(WINDOWSIZE)
PURPLE=(138,43,226)

while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False  
    screen.fill(PURPLE)
    pygame.display.update()

pygame.quit()
