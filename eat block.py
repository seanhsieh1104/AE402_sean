# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 10:08:48 2021

@author: Hsieh
"""

import pygame
import random
import time
black=(0,0,0)
white=(255,255,255)
green=(0,255,0)
red=(255,0,0)
purple=(255,0,255)


class Block(pygame.sprite.Sprite):
    def __init__(self,color,width,height):
        #從Block樣式裡，我們的目標是根據導入參數
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
    
pygame.init()
screenW = 700
screenH = 500
score = 0
play = True
font = pygame.font.Font(None, 30)
clock = pygame.time.Clock()
screen=pygame.display.set_mode([screenW,screenH])
#建立一個角色群組(Group)，將程式中的Block都加到此角色群組中(player、block)
Block_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()
for i in range(50):
    random_color = (random.randrange(1,255),random.randrange(1,255),random.randrange(1,255))
    block = Block(random_color,20,20)
    block.rect.x = random.randrange(screenW)
    block.rect.y = random.randrange(screenH)
    Block_list.add(block)
    #加block加到角色群組中
    all_sprites_list.add(block)
    #創造唯一的紅色player block，就將之加至pll_sprites_list角色群組中
player = Block(red,20,20)
all_sprites_list.add(player)
start_ticks = pygame.time.get_ticks()
pygame.display.set_caption("game")

# ---------Main Program loop--------------
while play:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            play = False
    screen.fill(white)
    all_sprites_list.draw(screen)
    seconds = int((pygame.time.get_ticks() - start_ticks)/1000)
    pos = pygame.mouse.get_pos()
    player.rect.x = pos[0]
    player.rect.y = pos[1]
    blocks_hit_list = pygame.sprite.spritecollide(player,Block_list,True)
    for block in blocks_hit_list:
        score += 1
    all_sprites_list.draw(screen)
    message = str(score) + 'point'
    text = font.render(message,10,black)
    screen.blit(text,(10,10))
    t = font.render(str(seconds),10,red)
    screen.blit(t,(10,40))
        
    if seconds > 9:
        text = font.render('Game Over',50,green)
        pos = 0
        time.sleep(2)
        print('Game Over')
        print('Score = ' + str(score))
        screen.blit(text,(100,100))
        play = False
    pygame.display.flip()
    clock.tick(60)
pygame.quit()