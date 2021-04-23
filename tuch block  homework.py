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
pygame.init()

size=(700,500)
screen=pygame.display.set_mode(size)
pygame.display.set_caption("game")

done = False
clock=pygame.time.Clock()
pos = (0,0)
playerX = 0
playerY = 0
playerW = 50
playerH = 50
blockW = 50
blockH = 50
blockX = []
blockY = []
collision = []
score = 0


for i in range(10):
    blockX.append(random.randrange(700))
    blockY.append(random.randrange(500))
    collision.append(False)

font = pygame.font.Font(None,50)
start_ticks = pygame.time.get_ticks()
screen.fill(white)
while not done:     
    for event in pygame.event.get():
            
        if event.type == pygame.QUIT:
            done = True  
    if score == 0:
        seconds = int((pygame.time.get_ticks() - start_ticks) / 1000)
    for i in range(10):
        xin = blockX[i] <= playerX <= blockX[i] * blockW or blockX[i] <= playerX + playerW <= blockX[i] * blockW
        yin = blockY[i] <= playerY <= blockY[i] * blockH or blockY[i] <= playerY + playerH <= blockY[i] * blockH
    pos = pygame.mouse.get_pos()  
    if xin and yin and not collision[i]:
        collision[i] = True
        score += 1
    playerX = pos[0]
    playerY = pos[1]
    screen.fill(white)
    pygame.draw.rect(screen,red,[playerX,playerY,playerW,playerH])
    for i in range(10):
        if not collision[i]:
            pygame.draw.rect(screen,black,[blockX[i],blockY[i],blockW,blockH])
    
    
    message = str(score) + ' point'
    text = font.render(message,10,black)
    screen.blit(text,(10,10))
    t = font.render(str(seconds),10,red)
    screen.blit(t,(100,100))
    clock.tick(60)
    GameOver= font.render('Complete',50,green)
    if score == 1:
        screen.blit(GameOver,(250,250))
        
    pygame.display.flip()
pygame.quit()