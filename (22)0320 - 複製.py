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
yellow = (255,255,0)

pygame.init()

size=(700,500)
screen=pygame.display.set_mode(size)
pygame.display.set_caption("game")

x = random.randint(0,700)
y = random.randint(0,500)

done=False
clock=pygame.time.Clock()
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
            
    screen.fill(white)
    
    pygame.draw.circle(screen,yellow,(350,250),50,50)
    pygame.draw.circle(screen,black,(370,240),10,10)
    pygame.draw.circle(screen,black,(330,240),10,10)
    pygame.draw.circle(screen,black,(350,280),20,10)
    pygame.draw.line(screen,yellow,(370,265),(330,265),30)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()