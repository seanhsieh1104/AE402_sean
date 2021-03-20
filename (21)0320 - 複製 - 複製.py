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
size=(700,500)
screen=pygame.display.set_mode(size)

pygame.display.set_caption("game")

snow_list = []

for i in range(50):
    x = random.randint(0,700)
    y = random.randint(0,500)
    snow_list.append([x,y])
    
done=False
    
    





clock=pygame.time.Clock()
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
    screen.fill(white)
    
    for i in range()
    pygame.display.flip()
    clock.tick(60)
pygame.quit()