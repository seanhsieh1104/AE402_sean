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
    pygame.draw.rect(screen,green,(350,250,200,100))
    pygame.draw.rect(screen,black,(500,190,50,70))
    pygame.display.flip()
    clock.tick(60)
pygame.quit()