from pygame import *
import os


back = (200, 255, 255)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)

workdir = os.getcwd()#! Добавитти
clock = time.Clock()


game=True
finish =False
FPS = 60

class GameSprite(sprite.Sprite):
    def __init__(self,pl_img,pl_x,pl_y,pl_speed,width, height):
        super().__init__()
        self.image = transform.scale(image.load(os.path.join(workdir,pl_img)),(width,height))
        self.speed = pl_speed
        self.rect = self.image.get_rect()
        self.rect.x = pl_x
        self.rect.y = pl_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y>5:
            self.rect.y -=self.speed
        if keys[K_s] and self.rect.y< win_height-80:
            self.rect.y +=self.speed

    def update_r(self):
        keys = key.get_pressed() #! Не пропустіть
        if keys[K_UP]:
            self.rect.y -=self.speed
        if keys[K_DOWN]:
            self.rect.y +=self.speed        

speed_x = 3
speed_y = 3

racket1 = Player('racket.png',30,200,4,50,150)
racket2 = Player('racket.png',520,200,4,50,150)
ball = GameSprite('tenis_ball.png',200,200,4,50,50)


font.init()
font = font.Font(None,35)
lose1 = font.render('PLAYER 1 LOSE!', True,(255,0,0))
lose2 = font.render('PLAYER 2 LOSE!', True,(255,0,0))
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish!=True:
        window.fill(back)
        racket1.update_l()
        racket2.update_r()
        ball.rect.x+=speed_x
        ball.rect.y+=speed_y
        if sprite.collide_rect(racket1,ball) or sprite.collide_rect(racket2,ball):
            speed_x*=-1
        if ball.rect.y > win_height-50 or ball.rect.y<0:
            speed_y*=-1
        if ball.rect.x> win_width:
            finish = True
            window.blit(lose2,(200,200))
        if ball.rect.x<0:
            finish = True
            window.blit(lose1,(200,200))
        racket1.reset()
        racket2.reset()
        ball.reset()
    display.update()
    clock.tick(FPS)
