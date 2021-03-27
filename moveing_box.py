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
pygame.init()
def move(image1,image2):
    global count
    if count < 5:
        image = image1
    if count >= 1:
        image = image2
    if count >= 10:
        count = 0
    else:
        count += 1
    return image
            
size=(700,500)
screen=pygame.display.set_mode(size)
pygame.display.set_caption("game")
done=False
clock=pygame.time.Clock()
x = 0
y = 0
w = 0
speed = 2
count = 0
locked = False
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
    keys = pygame.key.get_pressed()
    if not locked: 
        if keys[pygame.K_LEFT]:
            x = x - speed
        elif keys[pygame.K_RIGHT]:
            x = x + speed
        elif keys[pygame.K_UP]:
            y = y - speed
            w = w + 1
            speed = speed + 0.01
        elif keys[pygame.K_DOWN]:
            y = y + speed
            w = w - 1
            speed = speed - 0.01
        elif keys[pygame.K_SPACE]:
            locked = True
        else:
            pass
    else:
        if count < 10:
            count += 10
        else:
            x = random.randint(0,700)
            y = random.randint(0,500)
            locked = False
            count = 0
    screen.fill(white)
    
    pygame.draw.circle(screen,red,(x+10,y+10),w+10,w+10)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()