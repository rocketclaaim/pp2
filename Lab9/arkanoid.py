import pygame
import random
pygame.init()

class Ackanoid:
    # unb - number of unbreakable bricks, bon - bonus
    def __init__(self, w=1200, h=800, unb=0, bon=0):
        self.w = w
        self.h = h
        self.unb = unb
        self.bon = bon
        self.__pause_state = False # pause state
        self.__over_state = False # to prevent pause on gameover/win screen
        
        self.def_clr = (0, 255, 0)
        self.unb_clr = (255, 0, 0)
        self.bon_clr = (255, 255, 0)

        self.__loop()
    
    def __loop(self):

        while True:
            self.screen = pygame.display.set_mode((self.w, self.h))
            self.clock = pygame.time.Clock()

            self.__ball_init()
            self.__generate_ball()
            self.__generate_paddle()
            self.__generate_bricks()

            self.__sound()
            self.__score()
            self.__texts()
            self.shrink = pygame.time.get_ticks()

            restart = self.__game()

            if not restart:
                return

    def __pause(self):
        self.__draw_pause()
        self.__settings_btn()
        pygame.display.flip()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and not self.__over_state:
                        self.__pause_state = not self.__pause_state
                        return
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.settextRectb.collidepoint(event.pos):
                        self.__settings()
                        return

                    
    def __settings(self):
        self.__draw_settings()
        self.__draw_settings_menu()
        pygame.display.flip()

        while True:
            self.__draw_size()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and not self.__over_state:
                        self.__pause_state = not self.__pause_state
                        return
                    if event.key == pygame.K_RIGHT:
                        if self.ballRadius != 30:
                            self.ballRadius += 0.5
                    if event.key == pygame.K_LEFT:
                        if self.ballRadius != 0.5:
                            self.ballRadius -= 0.5
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.speedtextRect.collidepoint(event.pos):
                        self.shrink = pygame.time.get_ticks()
                        self.offset = pygame.time.get_ticks()
                    if self.regtextRect.collidepoint(event.pos):
                        self.__generate_bricks()


    def __game(self):
        self.__over_state = False
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and not self.__over_state:
                        self.__pause_state = not self.__pause_state
                    elif event.key == pygame.K_r:
                        return True

            key = pygame.key.get_pressed()
            self.screen.fill((0, 0, 0))

            if self.__pause_state:
                self.offset = pygame.time.get_ticks()
                self.__pause()
                self.shrink += (pygame.time.get_ticks() - self.offset)

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
                self.__over_state = True
                self.screen.blit(self.losetext, self.losetextRect)
            elif not len(self.block_list) - self.unb:
                self.screen.fill((255,255, 255))
                self.__over_state = True
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

    def __ball_init(self):
        self.ballSpeed = 6
        self.ballRadius = 20

    def __generate_ball(self):    
        ball_rect = int(self.ballRadius * 2 ** 0.5)
        self.ball_rect = ball_rect
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
        self.collision_sound = pygame.mixer.Sound(r'C:\Users\user\Desktop\PP2\Lab9\catch.mp3')
    
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
        self.__bigfont = pygame.font.SysFont('comicsansms', 40)
        self.__smallfont = pygame.font.SysFont('comicsansms', 25)
        btnrect = pygame.Rect(0, 0, 216, 35)

        # lose/win texts 
        self.losetext = self.__bigfont.render('Game over', True, (255, 255, 255))
        self.losetextRect = self.losetext.get_rect()
        self.losetextRect.center = (self.w // 2, self.h // 2)

        self.wintext = self.__bigfont.render('You win yay', True, (0, 0, 0))
        self.wintextRect = self.wintext.get_rect()
        self.wintextRect.center = (self.w // 2, self.h // 2)

        # pause text
        self.pausetext = self.__bigfont.render('Pause', True, (255, 255, 255))
        self.pausetextRect = self.pausetext.get_rect()
        self.pausetextRect.center = (self.w // 2, self.h // 2 - 100)

        # settings text menu
        self.settextw = self.__bigfont.render('Settings', True, (255, 255, 255))
        self.settextRectw = self.settextw.get_rect()
        self.settextRectw.center = (self.w // 2, self.h // 2 - 100)

        # settings text button
        self.settextb = self.__smallfont.render('Settings', True, (0, 0, 0))
        self.settextRectb = btnrect.copy()
        self.settextRectb.center = (self.w // 2, self.h // 2 + 50)

        self.speedtext = self.__smallfont.render('Reset paddle', True, (0, 0, 0))
        self.speedtextRect = btnrect.copy()
        self.speedtextRect.center = (self.w // 2, self. h // 2 + 50)

        self.regtext = self.__smallfont.render('Regenerate blocks', True, (0, 0, 0))
        self.regtextRect = btnrect.copy()
        self.regtextRect.center = (self.w // 2, self.h // 2 + 100)

        self.ballsizeRect = btnrect.copy()
        self.ballsizeRect.center = (self.w // 2, self.h // 2 + 150)

    def lose_draw(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.losetext, self.losetextRect)
    
    def win_draw(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.wintext, self.wintextRect)

    def __draw_pause(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.pausetext, self.pausetextRect)

    def __draw_settings(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.settextw, self.settextRectw)

    def __settings_btn(self):
        pygame.draw.rect(self.screen, (255, 255, 255), self.settextRectb)
        self.screen.blit(self.settextb, self.settextRectb)

    def __draw_settings_menu(self):
        pygame.draw.rect(self.screen, (255, 255, 255), self.speedtextRect)
        pygame.draw.rect(self.screen, (255, 255, 255), self.regtextRect)

        self.screen.blit(self.speedtext, self.speedtextRect)
        self.screen.blit(self.regtext, self.regtextRect)
        pygame.display.flip()

    def __draw_size(self):
        pygame.draw.rect(self.screen, (255, 255, 255), self.ballsizeRect)
        txt = self.__smallfont.render(f'Ball size: {self.ballRadius}', True, (0, 0, 0))

        self.screen.blit(txt, self.ballsizeRect)
        pygame.display.flip()
    
Ackanoid(unb=5, bon=2)