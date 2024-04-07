import pygame, sys
from pygame.locals import *
import random, time
# Инициализация
pygame.init()
# Настройка FPS
FPS = 60
FramePerSec = pygame.time.Clock()
# Создание цветов
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
# Другие переменные для использования в программе
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEEDENEMY = 5
SPEEDCOIN = 6
SPEEDCOIN2 = 5
SCORE = 0
NUMBERCOIN = 0
# Настройка шрифтов
font = pygame.font.Font(r'C:\Users\user\Desktop\PP2\Lab8\10922.otf', 90)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)
background = pygame.image.load(r"C:\Users\user\Desktop\PP2\Lab8\AnimatedStreet.png")
# Создайте белый экран
DISPLAYSURF = pygame.display.set_mode((400, 600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")
# Setting Enemy
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"C:\Users\user\Desktop\PP2\Lab8\Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0) #gde ono budet poyiavitca

    def move(self):
        #obivlyam score
        global SCORE
        #перемещает прямоугольник на место
        self.rect.move_ip(0, SPEEDENEMY)
        #esli enemy proshel ne kasaya player, togda score+=1
        if (self.rect.bottom > 600):
            SCORE += 1
            #dalshe enemy poyiavliatsa randomno eshe raz
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
#Setting Player
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"C:\Users\user\Desktop\PP2\Lab8\Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520) #gde ono budet poyiavitca
    def move(self):
        #dvizheniya na pravo na levo,top,botom
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)
# Setting Coin
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"C:\Users\user\Desktop\PP2\Lab8\coin.png")
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)#gde ono budet poyiavitca
        self.state = False

    def move(self):
        #obivlyam SPEEDCOIN
        global SPEEDCOIN
        #перемещает прямоугольник на место
        self.rect.move_ip(0, SPEEDCOIN)
        #poiyavlenya monet
        if (self.rect.bottom > 600 or self.state):
            SPEEDCOIN = 6
            self.state = False
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
class Coin2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"C:\Users\user\Desktop\PP2\Lab8\coin2.png")
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(20, SCREEN_WIDTH - 60), 0)#gde ono budet poyiavitca
        self.state = False

    def move(self):
        #obivlyam SPEEDCOIN
        global SPEEDCOIN2
        #перемещает прямоугольник на место
        self.rect.move_ip(0, SPEEDCOIN2)
        #poiyavlenya monet
        if (self.rect.bottom > 600 or self.state):
            SPEEDCOIN2 = 5
            self.state = False
            self.rect.top = 0
            self.rect.center = (random.randint(20, SCREEN_WIDTH - 60), 0)
# Setting up Sprites
P1 = Player()
E1 = Enemy()
C1 = Coin()
C2 = Coin2()
# Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
coins = pygame.sprite.Group()
coins.add(C1)
coins2 = pygame.sprite.Group()
coins2.add(C2)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)
all_sprites.add(C2)
# Игровая петля
while True:
    # Циклическое прохождение всех происходящих событий
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    #накладывать одно изображение на другое
    DISPLAYSURF.blit(background, (0, 0))
    #контейнер для хранения и управления несколькими объектами Sprite
    scores = font_small.render(str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10, 10))
    collect = font_small.render(str(NUMBERCOIN), True, BLACK)
    DISPLAYSURF.blit(collect, (SCREEN_WIDTH - 30, 10))
    #Перемещает и перерисовывает все спрайты
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()
    # Выполняется, если происходит столкновение между игроком и противником
    if pygame.sprite.spritecollideany(P1, enemies):
        #Простая проверка, пересекает ли спрайт что-либо в группе.
        pygame.mixer.Sound(r'C:\Users\user\Desktop\PP2\Lab8\crash.wav').play()
        time.sleep(1)

        DISPLAYSURF.fill(RED)
        pygame.mixer.Sound(r'C:\Users\user\Desktop\PP2\Lab8\game_over_theme.mp3').play()
        DISPLAYSURF.blit(game_over, (30, 250))

        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
            #удалить спрайт из всех групп
        time.sleep(4)
        pygame.quit()
        sys.exit()

    if pygame.sprite.spritecollideany(P1, coins):
        NUMBERCOIN += 1
        SPEEDENEMY += 1
        pygame.mixer.Sound(r'C:\Users\user\Desktop\PP2\Lab8\coin.mp3').play()
        for entity in coins:
            entity.state = True
    if pygame.sprite.spritecollideany(P1, coins2):
        NUMBERCOIN += 10
        pygame.mixer.Sound(r'C:\Users\user\Desktop\PP2\Lab8\coin.mp3').play()
        for entity in coins2:
            entity.state = True
    pygame.display.update()
    FramePerSec.tick(FPS)