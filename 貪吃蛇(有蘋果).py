# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 10:08:48 2021

@author: Hsieh
"""

import pygame
import time
import random
from queue import Queue
red=(255,0,0)
black=(0,0,0)
white=(255,255,255)
green=(0,255,0)

segment_width = 48
segment_height = 48
segment_margin = 2
segment_head_x = 0
segment_head_y = 0
x_change = 0.5
y_change = 0
score = 0
class Segment(pygame.sprite.Sprite):
    def __init__(self,x,y):
        color1 = random.randint(0,255)
        color2 = random.randint(0,255)
        color3 = random.randint(0,255)
        color = [color1,color2,color3]
        super().__init__()
        self.image = pygame.Surface([segment_width,segment_height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x*(segment_width+segment_margin)
        self.rect.y = y*(segment_height+segment_margin)
        self.x = x
        self.y = y
pygame.init()
screen = pygame.display.set_mode([800,600])
font = pygame.font.Font(None, 30)
size=(800,600)
screen=pygame.display.set_mode(size)
pygame.display.set_caption("貪吃蛇")
allspriteslist = pygame.sprite.Group()
snake_segments = Queue()
for i in range(5):
    x = 3 + i
    y = 3
    segment = Segment(x,y)
    snake_segments.put(segment)
    allspriteslist.add(segment)
    segment_head_x = x
    segment_head_y = y
done=False
clock=pygame.time.Clock()
eat = True
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
    if event.type==pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            x_change = (segment_width + segment_margin) *- 1
            y_change = 0
        if event.key == pygame.K_RIGHT:
            x_change = (segment_width + segment_margin)
            y_change = 0
        if event.key == pygame.K_UP:
            x_change = 0
            y_change = (segment_height + segment_margin) *- 1
        if event.key == pygame.K_DOWN:
            x_change = 0
            y_change = (segment_height + segment_margin)
    segment_head_x = segment_head_x + x_change
    segment_head_y = segment_head_y + y_change
    segment = Segment(segment_head_x,segment_head_y)
    snake_segments.put(segment)
    allspriteslist.add(segment)
    if eat:
        xa = random.randrange(16)
        ya = random.randrange(12)
        eat = False
    else:
        old_segment = snake_segments.get()
        allspriteslist.remove(old_segment)
    apple = Segment(xa,ya)
    if segment.x ==apple.x and segment.y == apple.y:
        score += 1
        pygame.display.set_caption('貪吃蛇| 分數:'+ str(score))
    screen.fill(black)
    allspriteslist.draw(screen)
    if segment_head_x >= 800 or segment_head_y >= 600 or segment_head_x <= 0 or segment_head_y <= 0:
        text = font.render('Game Over',50,green)
        screen.blit(text,(300,200))
        print('Game Over')
        pygame.display.flip()
        time.sleep(1)
        done = True
    pygame.draw.rect(screen,red,(xa*(segment_width+segment_margin),ya*(segment_width+segment_margin),segment_width,segment_height))
    allspriteslist.draw(screen)
    pygame.display.flip()
    clock.tick(5)
pygame.quit()