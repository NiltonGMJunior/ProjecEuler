# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 13:35:14 2017

@author: Nilton Junior
"""

sumSqr = 0 # Soma dos quadrados

sqrSum = 0 # Quadrado da soma

limit = 100

for i in range(0,limit):
    
    sumSqr = sumSqr + (i + 1)**2
    
    sqrSum = sqrSum + i + 1
    
sqrSum = sqrSum**2

diff = sqrSum - sumSqr

print(diff) 