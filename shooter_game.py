from pygame import *
from random import randint
import pygame
import pygame_menu
from pygame_menu import themes

font.init()
font1 = font.Font(None, 80)
win = font1.render('YOU WIN!', True, (255, 215, 0))
lose = font1.render('YOU LOSE!', True, (180, 0, 0))
font2 = font.Font(None, 36)


mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()
fire_sound = mixer.Sound('fire.ogg')


img_back = 'galaxy.jpg'
img_hero = 'rocket.png'
img_bullet = 'bullet.png'
img_enemy = 'ufo.png'
img_asteroid = 'asteroid.png'

score = 0
score2 = 0
lost = 0
lost2 = 0
max_lost = 3
life = 4
goal = 50
goal2 = 50

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)

        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed

        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        mousekey = mouse.get_pressed()
        if mousekey[0]:
            fire_sound.play()
            self.fire()
            self.fire()
        elif mousekey[2]:
            fire_sound.play()
            bullet = Bullet(img_bullet, self.rect.centerx, self.rect.top, 150, 305, -55)    
            bullets.add(bullet)
        else:
            x, y = mouse.get_pos()
            self.rect.x = x
    def fire(self):
        bullet = Bullet(img_bullet, self.rect.centerx, self.rect.top, 15, 20, -45)    
        bullets.add(bullet)

            

class Enemy1(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        

        if self.rect.y > win_height:
            self.rect.x = randint(80, win_width - 80)
            self.rect.y = 0
            lost = lost + 1

class Enemy2(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost2
        

        if self.rect.y > win_height:
            self.rect.x = randint(80, win_width - 80)
            self.rect.y = 0
            lost2 = lost2 + 1
            
class Bullet(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y < 0:
            self.kill()


win_width = 1000
win_height = 800
surface = display.set_mode((win_width, win_height))
display.set_caption('Maze')
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back), (win_width, win_height))
clock = time.Clock()
display.update()
FPS = 120

def set_difficulty(value, difficulty):
    print(value)
    print(difficulty)
 

ship = Player(img_hero, 5, win_height - 100, 80, 100, 10)

monsters = sprite.Group()
for i in range(1, 60):
    monster = Enemy1(img_enemy, randint(80, win_width - 80),  40, 80, 50, randint(1,10))
    monsters.add(monster)

asteroids = sprite.Group()
for i in range(1, 60):
    asteroid = Enemy2(img_asteroid, randint(80, win_width - 80),  40, 80, 50, randint(1,10))
    asteroids.add(asteroid)


bullets = sprite.Group()

finish = False
game = True


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                fire_sound.play
                ship.fire()
    sprites_list = sprite.groupcollide(monsters,  bullets, True, True)
    sprites_list1 = sprite.groupcollide(asteroids,  bullets, True, True)
    for hit in sprites_list:
        
        score += 1
    for hit in sprites_list1:
        score2 += 1

    sprites_list2 = sprite.spritecollide(ship, monsters, False)
    sprites_list3 = sprite.spritecollide(ship, asteroids, False)

    for hit in sprites_list2:
        life = life - 1
    for hit in sprites_list3:
        life = life - 1

    

 



    if not finish:

        window.blit(background, (0,0))
        if life == 0 or lost >= max_lost:
            finish = True
            window.blit(lose, (200, 200))
        if life == 0 or lost2 >= max_lost:
            finish = True
            window.blit(lose, (200, 200))
        if score >= goal:
            finish = True
            window.blit(win, (200, 200))
        if score2 >= goal2:
            finish = True
            window.blit(win, (200, 200))

 
        text = font2.render('Счет M:'+ str(score), 1,(255, 255, 255))
        window.blit(text, (10, 20))

        text = font2.render('Счет A:'+ str(score2), 1,(255, 255, 255))
        window.blit(text, (870, 20))

        text_lose = font2.render('Пропущено M:' + str(lost), 1, (255, 255, 255))
        window.blit(text_lose, (270, 0))
        text_lose = font2.render('Пропущено A:' + str(lost2), 1, (255, 255, 255))
        window.blit(text_lose, (570, 0))


        ship.update()
        monsters.update()
        bullets.update()
        asteroids.update()

        ship.reset()
        monsters.draw(window)
        bullets.draw(window)
        asteroids.draw(window)

        display.update()

        time.delay(50)

