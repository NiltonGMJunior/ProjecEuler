# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 13:15:56 2017

@author: Nilton Junior
"""

n = 1000 # Limite da sequência

s = 0 # Armazena o resultado da soma

for i in range(0,n - 1):
    
    if  (       (i + 1) % 3 == 0
         or     (i + 1) % 5 == 0
        ):
            
        
#            print (i + 1)
            
            s = s + i + 1

print(s)

