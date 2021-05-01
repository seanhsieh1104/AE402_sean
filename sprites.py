# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 10:08:48 2021

@author: Hsieh
"""

import pygame
import random
black=(0,0,0)
white=(255,255,255)
green=(0,255,0)
red=(255,0,0)
purple=(255,0,255)
random_color = (random.randrange(1,255),random.randrange(1,255),random.randrange(1,255))

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
screen=pygame.display.set_mode([screenW,screenH])
#建立一個角色群組(Group)，將程式中的Block都加到此角色群組中(player、block)
Block_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()
for i in range(50):
    block = Block(black,20,20)
    block.rect.x = random.randrange(screenW)
    block.rect.y = random.randrange(screenH)
    #加block加到角色群組中
    all_sprites_list.add(random_color)
    #創造唯一的紅色player block，就將之加至pll_sprites_list角色群組中
player = Block(red,20,20)
all_sprites_list.add(player)
play = True

pygame.display.set_caption("game")
done=False
clock = pygame.time.Clock()
# ---------Main Program loop--------------
while play:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            play = False
    screen.fill(white)
    all_sprites_list.draw(screen)
    #顯示出所有角色
    pygame.display.flip()
    clock.tick(60)
pygame.quit()