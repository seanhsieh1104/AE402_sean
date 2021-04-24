# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 10:51:24 2021

@author: Hsieh
"""
class human():
    def __init__(self,name,weight,height):
        self.name = name
        self.weight = weight
        self.height = height
    def bmi(self):
        return self.weight / ((self.height/100)**2)
        
class woman(human):
    def __init__(self,name,weight,height,bust,waist,hip):
        super().__init__(name,weight,height)
        self.bust = bust
        self.waist = waist
        self.hip = hip
        
    def bwh(self):
        print('bust={},waist={},hip={}'.format(self.bust,self.waist,self.hip))
        
class man(human):
    def __init__(self,name,weight,height,military):
        super().__init__(name,weight,height)
        self.military = military
        
    def description(self):
        if self.military:
            print('he is/was a selider')
        else:
            print('he is/was not a selider')