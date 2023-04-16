import pygame
score_val = 0
    scoreX = 5
    scoreY = 5
    scoreY1 = 20
    health = 3
    
    
    pygame.init()
    font = pygame.font.Font('freesansbold.ttf', 20)
    
    win_width = 800
    win_height = 500

    def show_score(x, y):
        score = font.render("Points: " + str(score_val),
                            True, (255,255,255))
        
        screen.blit(score, (x , y ))

    def hp(x, y):
        hp1 = font.render("❤: " + str(health),
                            True, (255,255,255))
        
        screen.blit(hp1, (x , y ))

    class GameSprite(sprite.Sprite):
        def __init__(self, player_Image, player_x, player_y, player_speed):
            super().__init__()
            self.image = transform.scale(image.load(player_Image), (50, 50))
            self.speed = player_speed


            self.rect = self.image.get_rect()
            self.rect.x = player_x
            self.rect.y = player_y

        def reset(self):
            screen.blit(self.image, (self.rect.x, self.rect.y))
    class Player1(pygame.sprite.Sprite):
        def __init__(self, player_Image, player_x, player_y, player_speed):
            super().__init__()
            self.image = pygame.transform.scale(pygame.image.load(player_Image), (50, 50))
            self.speed = player_speed


            self.rect = self.image.get_rect()
            self.rect.x = player_x
            self.rect.y = player_y


        def update(self):
            self.speedx = 0
            keystate = pygame.key.get_pressed()
            if keystate[pygame.K_LEFT]:
                self.speedx = -8
            if keystate[pygame.K_RIGHT]:
                self.speedx = 8
            self.rect.x += self.speedx
            if self.rect.right > win_width:
                self.rect.right = win_width
            if self.rect.left < 0:
                self.rect.left = 0

        def shoot(self):
            bullet = Bullet(self.rect.centerx, self.rect.top)
            all_sprites.add(bullet)
            bullets.add(bullet)

    class Mob(GameSprite):
            
            def update(self):
                
                
                
                self.rect.y += self.speed
                if self.rect.y >= win_height:
                    self.rect.x = randint(80, 700)
                    self.rect.y = 0 
                   
                    
                if self.rect.right > win_width:
                    self.rect.right = win_width
                if self.rect.left < 0:
                    self.rect.left = 0
            
    class Bullet(pygame.sprite.Sprite):
        def __init__(self, x, y):
            pygame.sprite.Sprite.__init__(self)
            self.image = bullet_img
            self.image.set_colorkey('BLACK')
            self.rect = self.image.get_rect()
            self.rect.bottom = y
            self.rect.centerx = x
            self.speedy = -10

        def update(self):
            self.rect.y += self.speedy
            if self.rect.bottom < 0:
                self.kill()

    img_back = "galaxy.png"
    background = pygame.transform.scale(pygame.image.load(img_back), (800,500))
    background_rect = background.get_rect()


   
    bullet_img = pygame.transform.scale(pygame.image.load('bullet.png'),(10,10))

    all_sprites = pygame.sprite.Group()
    mobs = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    player = Player1(filename_pers,580, 420, 0)
    all_sprites.add(player)
    for i in range(2):
        m = Mob('ufo.png',randint(80, win_width - 80),1, randint(1,3))
        all_sprites.add(m)
        mobs.add(m)

    running = True
    while running:
        
        
        
        for event in pygame.event.get():
        
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.shoot()
                    piu.play()
            
        
        hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
        for hit in hits:
            score_val += 1
            m = Mob('ufo.png',randint(80, win_width - 80),500, randint(1,4))
            all_sprites.add(m)
            mobs.add(m)

        
        
        if sprite.collide_rect(player, m):
            
            health = health - 1
            m.kill()
        if health < 0:
            
            screen.blit(lose, (50, 200))
            display.update()
            time.delay(3500)
            display.update()
            quit()
        all_sprites.update()
        
        if score_val == 5:
                
            screen.blit(liw, (50, 200))
            display.update()
            time.delay(3500)
            
            lvl4()
            
            display.update()
            quit()
        
            

        
        screen.blit(background, background_rect)
        all_sprites.draw(screen)
        show_score(scoreX, scoreY)
        hp(scoreX, scoreY1)
        pygame.display.update()              