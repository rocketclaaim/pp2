import pygame
import  sys
pygame.init()
SCREEN_WIDTH=800
SCREEN_HEIGHT=600
screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
white=(255,255,255)
screen.fill(white)
pygame.display.set_caption('ball')
BALL_RADIUS=25
BALL_DIAMETER = BALL_RADIUS*2
ball_x=SCREEN_HEIGHT//2
ball_y=SCREEN_WIDTH//2
SPEED=20
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
            pygame.quit()
            sys.exist()

        keys=pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            if ball_y-SPEED>=BALL_RADIUS:
                ball_y-=SPEED
        if keys[pygame.K_DOWN]:
            if ball_y-SPEED<=SCREEN_HEIGHT-BALL_RADIUS:
                ball_y+=SPEED
        if keys[pygame.K_LEFT]:
            if ball_x-SPEED>=BALL_RADIUS:
                ball_x-=SPEED
        if keys[pygame.K_RIGHT]:
            if ball_x<=SCREEN_WIDTH-BALL_RADIUS:
                ball_x+=SPEED
        pygame.draw.circle(screen, 'Red', (ball_x, ball_y), BALL_RADIUS)
        pygame.display.update()