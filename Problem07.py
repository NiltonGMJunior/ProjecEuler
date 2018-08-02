# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 13:35:14 2017

@author: Nilton Junior
"""

def isPrime(n):
    
    if n > 1:
        
        if  n % 2 == 0:
            
            if n == 2:
                
                tf = True
                
            else:
                
                tf = False
        
        else:
            
            tf = True
            
            i = 3
            
            while  (   i < n 
                   and tf == True
                   ):
                
                if n % i == 0:
                    
                    tf = False
                    
                else:
                    
                    i = i + 1
                    
    else:
        
        tf = False
                    
    return tf

c = 2 # Contador de primos, já cosniderando 2 e 3 como os primeiros

n = 3 # Primeiro valor a ser testado

while c < 10001:
    
    n = n + 2
    
    if(isPrime(n) == True):
        
        c = c + 1
        
        print("O primo " + str(c) + " é equivalenet a: " + str(n))




