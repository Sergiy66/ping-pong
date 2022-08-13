from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,p_speed,widht,height):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(widht,height))
        self.speed = p_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x()
        self.rect.y = player_y()
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

class Player(GameSprite):
    pass




win_wight = 600
win_height = 500
window = display.set_mode((win_wight, win_height))
blue = (200,255,255)
window.fill(blue)
display.set_caption("ping pong")

clock = time.Clock()
fps = 60
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    display .update()
    clock.tick(60)
