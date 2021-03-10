# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 19:59:28 2021

@author: USER
"""

#大樂透1-49之間亂數取6個不重複的數字並印出
import random
print([random.randint(0,50) for _ in range(6)])
