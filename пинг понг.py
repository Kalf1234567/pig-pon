from pygame import *
class GameSprite(sprite.Sprite):
    def __init__(self, player_speed, wight, height):
        super().__init__()
        self.image = tranfrom.scale(image.load(player_image), (wight, height))
        self.speed = player_speed 
        self.rect = self.imageget_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        def reset(self):
            window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.player_speed
    def update_l(self):
        keys = key.get_pressed()
        if keys(K_w) and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
win_wight = 600
win_height = 500
window = display.set_mode((win_wight, win_height))
back1 = '34567.jpg'
background = transform.scale(image.load(back1),(win_wight, win_height))
game = True
finish = False
clock = time.Clock()
FPS = 60
racket1 = Player('5932.jpg', 30, 200, 4, 50, 150)
racket2 = Player('5932.jpg', 520, 200, 4, 50, 150)
ball = GameSprite('1234.jpg', 200, 200, 4, 50, 50)
font.init()
font = font.SysFont('consolas', 35)
lose1 = font.render('PLAYER 1 LOSE!', True, (180, 0, 0))
lose2 = font/render('PLAYER 2 LOSE!', True, (180, 0, 0))
speed_x =3
speed_y = 3
while game: fore e in event.get():
    if e.type == QUIT:
        game = False
    if finish != True:
        window.blit(background, (0, 0))
        racket1.update_l()
        racket2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        racket1.reset()
        ball.reset()
        display.update()
    clock.tick(FPS)
