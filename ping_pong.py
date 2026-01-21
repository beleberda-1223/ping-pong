from pygame import *

green = (102, 255, 102)
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(green)
display.set_caption('Ping_pong')



class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y,  size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.speed = player_speed

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y < 400:
            self.rect.y += self.speed
        if keys[K_s] and self.rect.y > 100:
            self.rect.y += self.speed

    def update_l(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y < 400:
            self.rect.y += self.speed
        if keys[K_DOWN] and self.rect.y > 100:
            self.rect.y += self.speed

clock = time.Clock()
FPS = 60

player_1 = Player('racket.png', 0, 400, 30, 100, 3)
player_2 = Player('racket.png', 670, 400, 30, 100, 3)
ball = GameSprite('ball.png', 350, 250, 50, 50, 5)

run = True
finish = False

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    

    player_1.update_r()
    player_1.reset()
    player_2.update_l()
    player_2.reset()
    ball.update()
    ball.reset()


    display.update()
    clock.tick(FPS)
