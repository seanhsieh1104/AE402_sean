# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 10:08:48 2021

@author: Hsieh
"""

import pygame
black=(0,0,0)
white=(255,255,255)
green=(0,255,0)
red=(255,0,0)
purple=(255,0,255)

def recursive_rect(x,y,weidh,hight):
    pygame.draw.rect(screen,hight,[x,y,weidh,hight],3)
    
    if wiedh > 14:
        x = weidh * 0.1
        y = hight * 0.1
        hight = 0.8
        weidh = 0.8
        recursive_draw(x,y,weidh,hight)

pygame.init()

size=(700,500)
screen=pygame.display.set_mode(size)
pygame.display.set_caption("game")
done=False
clock=pygame.time.Clock()
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
    screen.fill(white)
    
    pygame.display.flip()
    clock.tick(60)
pygame.quit()