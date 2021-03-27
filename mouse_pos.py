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
def randomcolor():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)

size=(700,500)
screen=pygame.display.set_mode(size)
pygame.display.set_caption("game")
done = False
clock=pygame.time.Clock()
color = randomcolor()
count = 0
click = False
limit = 40
pos = (0,0)
while not done:     
    screen.fill(black)   
    if click and count < limit:
        pygame.draw.circle(screen,color,pos,count)
        count += 2
        if count >= limit:
            click = False
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            click = True
            count = 0
            color = randomcolor()
        if event.type == pygame.QUIT:
            done = True        
    pygame.display.flip()
    clock.tick(60)
pygame.quit()