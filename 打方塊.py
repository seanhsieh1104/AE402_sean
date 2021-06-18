# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 10:01:04 2021

@author: Hsieh
"""
import pygame
import random
import math
import time
class Ball(pygame.sprite.Sprite):
    dx = 0
    dy = 0
    x = 0
    y = 0
    direction = 0
    speed = 0
    
    def __init__(self,sp,srx,sry,radium,color):
        pygame.sprite.Sprite.__init__(self)
        self.speed = sp
        self.x = srx
        self.y = sry
        self.image = pygame.Surface([radium*2,radium*2])
        self.image.fill((110,30,40))
        pygame.draw.circle(self.image,color,(radium,radium),radium,0)
        self.rect = self.image.get_rect()
        self.rect.center = (srx,sry)
        self.direction = random.randint(60,100)
        
    def update(self):
        radian = math.radians(self.direction)
        self.dx = self.speed * math.cos(radian)
        self.dy = -self.speed * math.sin(radian)
        self.x += self.dx
        self.y += self.dy
        self.rect.x = self.x
        self.rect.y = self.y
        if(self.rect.left <= 0 or self.rect.right >= screen.get_width()-10):
            self.bouncelr()
        elif(self.rect.top <= -10):
            self.rect.top = 10
            self.bounceup()
        elif(self.rect.bottom >= screen.get_height()-10):
            return True
        else:
            return False
    def bouncelr(self):
        self.direction = (180 - self.direction) % 360
    def bounceup(self):
        self.direction = 360 - self.direction
class Brick(pygame.sprite.Sprite):
    def __init__(self,color,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([38,13])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = int((screen.get_width() - self.rect.width)/2)
        self.rect.y = screen.get_height() - self.rect.height - 20
        
    def update(self):
        pos = pygame.mouse.get_pos()
        self.rect.x = pos[0]
        if self.rect.x > screen.get_width() - self.rect.width:
            self.rect.x = screen.get_width() - self.rect.width
class Pad(pygame.sprite.Sprite):
    def __init__(self,color,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('pad.png')
        self.image.convert()
        self.rect = self.image.get_rect()
        self.rect.x = int((screen.get_width() - self.rect.width)/2)
        self.rect.y = screen.get_height() - self.rect.height - 20
    def update(self):
        pos = pygame.mouse.get_pos()
        self.rect.x = pos[0]
        if self.rect.x > screen.get_width() - self.rect.width:
            self.rect.x = screen.get_width() - self.rect.width
def gameover(message):
    global running
    text = font1.render(message,True,(255,0,255))
    screen.blit(text,(screen.get_width()/2-100,screen.get_height()/2-20))
    pygame.display.update()
    time.sleep(3)
    running = False
    
pygame.init()
score = 0
font = pygame.font.Font(None,30)
font1 = pygame.font.Font(None,35)
soundhit = pygame.mixer.Sound('hit.wav')
soundpad = pygame.mixer.Sound('pad.wav')
screen = pygame.display.set_mode((600,400))
pygame.display.set_caption('建立及使用角色')
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((255,255,255))
allsprite = pygame.sprite.Group
bricks = pygame.sprite.Group()
ball = Ball(10,300,350,10,(255,0,0))
allsprite.add(ball)
pad = Pad()
allsprite.add(pad)
clock = pygame.time.Clock()
for row in range(0,4):
    for column in range(0,15):
        if row == 0 or row == 1:
            brick = Brick((0,255,0),column * 40 + 1,row * 15 + 1)
        if row == 2 or row ==3:
            brick = Brick((0,0,255),column * 40 +1,row * 15 + 1)
running = True
while running:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    buttons = pygame.mouse.get_pressed()
    if buttons[0]:
        playing = True
    if playing == True:
        screen.blit(background,(0,0))
        fail = ball.update()
        if fail:
            gameover('Gameover')
        pad.update()
        hitbrick = pygame.sprite.spritecollide(ball,bricks,True)
        if len(hitbrick) > 0:
            score += len(hitbrick)
            soundhit.play()
            ball.rect.y += 20
            ball.bounceup()
            if len(bricks) == 0:
                gameover('Gameover')
        hitpad = pygame.sprite.collide_rect(ball,pad)
        if hitpad:
            soundpad.play()

    pygame.display.update()
pygame.quit()