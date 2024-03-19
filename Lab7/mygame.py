import pygame
pygame.init()
screen=pygame.display.set_mode((600,600))
pygame.display.set_caption("clock")
mickey=pygame.image.load('C:\Users\user\Desktop\PP2\mickey.png')
running=True
while running:
    screen.blit(mickey,(500,200))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
            pygame.quit()