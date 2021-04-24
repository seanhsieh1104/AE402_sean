# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 11:27:53 2021

@author: Hsieh
"""

import human

a = human.human('David',70,100)
print(a.name,'bmi:',a.bmi())

b = human.woman('Jenny', 95,160,30,20,30)
print(b.name,'bmi:',b.bmi())

c = human.man('Alex',68,179,True)
print(c.name,'bmi:',c.bmi())
c.description()