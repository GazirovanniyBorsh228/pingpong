from pygame import *
'''Необходимые классы'''


#класс-родитель для спрайтов
class GameSprite(sprite.Sprite):
   #конструктор класса
    def __init__(self, player_x, player_y, player_speed, width, height, player_image = None):
        super().__init__()
        self.image = Surface((width, height))
        self.image.fill((0, 0, 0))
        # каждый спрайт должен хранить свойство image - изображение
        if player_image:
            self.image = transform.scale(image.load(player_image), (55, 55))
        self.speed = player_speed
        # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y


    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


#класс-наследник для спрайта-игрока (управляется стрелками)
class Player(GameSprite):
    def update1(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update2(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    



#Игровая сцена:
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Maze")
window.fill((200, 250, 250))
#Персонажи игры:
player1 = Player(30, 200, 4, 50, 150)
player2 = Player(520, 200, 4, 50, 150)
ball = GameSprite(200, 200, 4, 50, 50, 'ball.png')

game = True
finish = False
clock = time.Clock()
FPS = 60


font.init()

font = font.Font(None, 70)
lose1 = font.render('player1 loser', True, (180, 0, 0))
lose2 = font.render('player2 loser', True, (180, 0, 0))

speed_x = 5
speed_y = 5
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    if finish != True:
        window.fill((200, 250, 250))
        player1.update1()
        player2.update2()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y *= -1
        if sprite.collide_rect(player1, ball) or sprite.collide_rect(player2, ball):
            speed_x  *= -1
        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))
        if ball.rect.x > 550:
            finish = True
            window.blit(lose2, (200, 200))
        player1.reset()
        player2.reset()
        ball.reset()
    display.update()
    clock.tick(FPS)
