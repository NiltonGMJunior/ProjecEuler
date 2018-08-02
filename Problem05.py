# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 13:15:56 2017

@author: Nilton Junior
"""
def isEvenlyDivisible(n,a,b):
    
    tf = True
    
    i = a
    
    while   (   i <= b
            and tf == True
            ):
        
        if n % i != 0:
            
            tf = False
            
        i = i + 1
    
    return tf

ref = 1

n = 1

tf = False

while tf == False:
    
    if isEvenlyDivisible(n,1,20) == True:
        
        tf = True
        
        ref = n
        
    n = n + 1
    
print(ref)
        

                
                
        
        
    

            



                            
            

    