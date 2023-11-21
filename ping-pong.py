from pygame import *

width = 600
height = 500
window = display.set_mode((width, height))

bg = (66, 245, 185)

clock = time.Clock()

stopped = False

class GameSprite(sprite.Sprite):
    def __init__(self, img, x, y, w, h, speed):
        super().__init__()
        self.image = transform.scale(image.load(img), (w, h))
        self.speed = speed

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_1(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.bottom < height:
            self.rect.y += self.speed
    
    def update_2(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.bottom < height:
            self.rect.y += self.speed

player_1 = Player("racket.png", 30, 200, 50, 150, 4)
player_2 = Player("racket.png", 520, 200, 50, 150, 4)

player_group = sprite.Group()
player_group.add(player_1)
player_group.add(player_2)

while stopped == False:
    for e in event.get():
        if e.type == QUIT:
            stopped = True


    window.fill(bg)
    player_group.draw(window)

    player_1.update_1()
    player_2.update_2()
    display.update()
    clock.tick(60)
