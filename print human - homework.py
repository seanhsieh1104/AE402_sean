# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 11:27:53 2021

@author: Hsieh
"""

import human

a = human.human('dog',2.5,32)
print(a.name,'bmi:',a.bmi())


c = human.man('cat',2,28,False)
print(c.name,'bmi:',c.bmi())
c.description()
