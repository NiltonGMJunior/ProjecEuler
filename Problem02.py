# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 13:15:56 2017

@author: Nilton Junior
"""

limit = 4000000 # Limite da contagem

f_old = 1 # 1o termo da sequência de Fibonacci

f_older = 1 # 2o termo da sequência de Fibonacci

f_new = f_old + f_older # 3o termo da sequência de Fibonacci

s = 2 # Soma dos elementos da sequência de Fibonacci pares menores do que o limite

while f_new < limit:
    
    temp = f_old  # Variável temporária
    
    f_old = f_new
    
    f_older = temp
    
    f_new = f_old + temp
    
    if f_new % 2 == 0:
        
        s = s + f_new
        
print(s)
    
    
