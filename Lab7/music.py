import pygame
pygame.init()
screen=pygame.display.set_mode((800,600))
pygame.display.set_caption('music')
koma='Lab7/koma.mp3'
rocket='Lab7/rocket.mp3'
liven='Lab7/travis.mp3'
music=[koma,rocket,liven]
aaa=0
pygame.mixer.music.load(music[aaa])
pygame.mixer.music.play()
running=True
play=False
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                play=not play
                if play:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
            elif event.key==pygame.K_RIGHT:
                aaa+=1
                if aaa==len(music):
                    aaa=0
                pygame.mixer.music.load(music[aaa])
                pygame.mixer.music.play()
            elif event.key==pygame.K_LEFT:
                aaa-=1
                if aaa==-1:
                    aaa=len(music)-1
                    pygame.mixer.music.load(music[aaa])
                    pygame.mixer.muxic.play()
pygame.display.flip


