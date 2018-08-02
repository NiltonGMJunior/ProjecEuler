# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 13:15:56 2017

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

target = 600851475143

i = 3
 
p = 1 # Maior fator primo de target

prod = 1 # Produto dos primos, usado para diminuir o tempo de processamento

while prod < target:
    
    if isPrime(i) == True:
        
        if target % i == 0:
            
            p = i
            prod = prod*p
            
            print(p)
            
    i = i + 2
    

            



                            
            

    