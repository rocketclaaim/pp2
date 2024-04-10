import pygame
import random

class Ackanoid:
    # unb - number of unbreakable bricks, bon - bonus
    def __init__(self, w=1200, h=800, unb=0, bon=0):
        self.w = w
        self.h = h
        self.unb = unb
        self.bon = bon
        
        self.def_clr = (0, 255, 0)
        self.unb_clr = (255, 0, 0)
        self.bon_clr = (255, 255, 0)

        self.__loop()
    
    def __loop(self):

        while True:
            pygame.init()
            self.screen = pygame.display.set_mode((self.w, self.h), pygame.RESIZABLE)
            self.clock = pygame.time.Clock()
            
            self.__generate_ball()
            self.__generate_paddle()
            self.__generate_bricks()

            self.__sound()
            self.__score()
            self.__texts()
            self.shrink = 0

            restart = self.__game()

            if not restart:
                return

    def __game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False
            key = pygame.key.get_pressed()
            
            if key[pygame.K_ESCAPE]:
                return False
            elif key[pygame.K_r]:
                return True

            self.screen.fill((0, 0, 0))

            pygame.draw.rect(self.screen, pygame.Color(255, 255, 255), self.paddle)

            pygame.draw.circle(self.screen, pygame.Color(255, 0, 0), self.ball.center, self.ballRadius)

            self.__bricks_draw()
            
            self.ball.x += self.ballSpeed * self.dx
            self.ball.y += self.ballSpeed * self.dy
            #Collision left 
            if self.ball.centerx < self.ballRadius or self.ball.centerx > self.w - self.ballRadius:
                self.dx = -self.dx
            #Collision top
            if self.ball.centery < self.ballRadius + 50: 
                self.dy = -self.dy
            #Collision with paddle
            if self.ball.colliderect(self.paddle) and self.dy > 0:
                self.dx, self.dy = self.__detect_collision(self.dx, self.dy, self.ball, self.paddle)

            #Collision blocks
            hitIndex = self.ball.collidelist(self.block_list)

            if hitIndex != -1:
                hitColor = self.color_list[hitIndex]
                # breakable and bonus - bonus block resets shrinking
                if hitColor == self.def_clr or hitColor == self.bon_clr:
                    hitRect = self.block_list.pop(hitIndex)
                    hitColor = self.color_list.pop(hitIndex)
                    self.dx, self.dy = self.__detect_collision(self.dx, self.dy, self.ball, hitRect)

                    if hitColor == self.bon_clr:
                        self.game_score += 4
                        self.shrink = pygame.time.get_ticks()
                    self.game_score += 1
                # unbreakable block
                elif hitColor == self.unb_clr:
                    hitRect = self.block_list[hitIndex]
                    self.dx, self.dy = self.__detect_collision(self.dx, self.dy, self.ball, hitRect)
                
                self.collision_sound.play()
                
            #Game score
            self.__score_draw()

            #Win/lose screens
            if self.ball.bottom > self.h:
                self.screen.fill((0, 0, 0))
                self.screen.blit(self.losetext, self.losetextRect)
            elif not len(self.block_list) - self.unb:
                self.screen.fill((255,255, 255))
                self.screen.blit(self.wintext, self.wintextRect)
            
                # increasing speed
                time = pygame.time.get_ticks()
                self.paddleSpeed = 20 + (time - self.shrink) // 1000

                # shrinking paddle 
                self.__change_paddle(150 - (time - self.shrink) // 1000, 25)

            #Paddle Control
            key = pygame.key.get_pressed()
            if key[pygame.K_LEFT] and self.paddle.left > 0:
                self.paddle.left -= self.paddleSpeed
            if key[pygame.K_RIGHT] and self.paddle.right < self.w:
                self.paddle.right += self.paddleSpeed


            pygame.display.flip()
            self.clock.tick(60)

    def __generate_ball(self):
        self.ballSpeed = 6

        ballRadius = 20
        ball_rect = int(ballRadius * 2 ** 0.5)

        self.ball_rect = ball_rect
        self.ballRadius = ballRadius
        self.ball = pygame.Rect(random.randrange(ball_rect, self.w - ball_rect), self.h // 2, ball_rect, ball_rect)
        self.dx, self.dy = 1, -1

    def __generate_paddle(self):
        self.paddleW = 150
        self.paddleH = 20
        self.paddleSpeed = 20
        self.paddle = pygame.Rect(self.w // 2 - self.paddleW // 2, self.h - self.paddleH - 30, self.paddleW, self.paddleH)
    
    def __change_paddle(self, paddleW=150, paddleH=25):
        self.paddleW = paddleW
        self.paddleH = paddleH

        left = self.paddle.left
        top = self.paddle.top
        self.paddle = pygame.Rect(left, top, self.paddleW, self.paddleH)
    
    def __score(self):
        self.game_score = 0
        game_score_fonts = pygame.font.SysFont('comicsansms', 40)
        self.game_score_fonts = game_score_fonts
    
    def __score_draw(self):
        game_score_text = self.game_score_fonts.render(f'Your game score is: {self.game_score}', True, (255, 255, 255))
        
        game_score_rect = game_score_text.get_rect()
        game_score_rect.center = (210, 20)
        self.screen.blit(game_score_text, game_score_rect)

    def __bricks_draw(self):
        [pygame.draw.rect(self.screen, self.color_list[color], block)
        for color, block in enumerate (self.block_list)]

    def __sound(self):
        self.collision_sound = pygame.mixer.Sound(r'C:\Users\user\Desktop\PP2\Lab8\catch.mp3')
    
    def __detect_collision(self, dx, dy, ball, rect):
        if dx > 0:
            delta_x = ball.right - rect.left
        else:
            delta_x = rect.right - ball.left
        if dy > 0:
            delta_y = ball.bottom - rect.top
        else:
            delta_y = rect.bottom - ball.top

        if abs(delta_x - delta_y) < 10:
            dx, dy = -dx, -dy
        if delta_x > delta_y:
            dy = -dy
        elif delta_y > delta_x:
            dx = -dx
        return dx, dy

    def __generate_bricks(self):
        self.block_list = []
        unb_coords = []
        self.color_list = []
        bon_coords = []

        for _ in range(self.unb):
            c = (random.randint(0, 9), random.randint(0, 3))
            while c in unb_coords:
                c = (random.randint(0, 9), random.randint(0, 3))
            unb_coords.append(c)
        
        for _ in range(self.bon):
            c = (random.randint(0, 9), random.randint(0, 3))
            while c in unb_coords or c in bon_coords:
                c = (random.randint(0, 9), random.randint(0, 3))
            bon_coords.append(c)

        for i in range(10):
            for j in range(4):
                if (i, j) in unb_coords:
                    self.color_list.append(self.unb_clr)
                elif (i, j) in bon_coords:
                    self.color_list.append(self.bon_clr)
                else:
                    self.color_list.append(self.def_clr)
                self.block_list.append(pygame.Rect(10 + 120 * i, 50 + 70 * j, 100, 50))

    def __texts(self):
        losefont = pygame.font.SysFont('comicsansms', 40)
        losetext = losefont.render('Game Over', True, (255, 255, 255))
        losetextRect = losetext.get_rect()
        losetextRect.center = (self.w // 2, self.h // 2)

        winfont = pygame.font.SysFont('comicsansms', 40)
        wintext = winfont.render('You win yay', True, (0, 0, 0))
        wintextRect = wintext.get_rect()
        wintextRect.center = (self.w // 2, self.h // 2)

        self.losetext = losetext
        self.losetextRect = losetextRect

        self.wintext = wintext
        self.wintextRect = wintextRect

    def lose_draw(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.losetext, self.losetextRect)
    
    def win_draw(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.wintext, self.wintextRect)

Ackanoid(unb=5, bon=2)