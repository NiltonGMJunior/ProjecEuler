# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 13:35:14 2017

@author: Nilton Junior
"""

def isPythegoreanTriplet(a,b,c):
    
    if a**2 + b**2 == c**2:
        
        tf = True
        
    else:
        
        tf = False
        
    return tf

tf = False

for a in range(0,1000):
         
    for b in range(a + 1, 1000):
    
            c = 1000 - a - b
            
            if isPythegoreanTriplet(a,b,c) == True:
                    
                print(a*b*c)

            

