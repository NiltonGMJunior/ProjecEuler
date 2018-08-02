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
                    
                    i = i + 2
                    
    else:
        
        tf = False 
                    
    return tf

c = 2 # Contador de primos, já cosniderando 2 e 3 como os primeiros

n = 3 # Primeiro valor a ser testado

s = 2 + 3 # Soma dos números primos, incluindo 2 e 3

while n < 2000000:
    
    n = n + 2
    
    if(isPrime(n) == True):
         
        c = c + 1
        
        s = s + n
        
        print("O primo " + str(c) + " é equivalenet a: " + str(n) + " e a soma dos " + str(c) + " primeiros primos é " + str(s))


'''

RUNDOWN SUMMARY:
BIGGEST PRIME BELOW 2 MILLION IS 1.999.993
IT IS THE 148.933th PRIME
THE SUM OF ALL PRIMES BELOW 2 MILLION IS 142.913.828.922

NOTICE!
THE CODE IS VERY INEFFICIENT AND OTHER WAYS OF FINDING PRIME NUMBERS SHOULD BE CONSIDERED IN ORDER TO ACHIEVE A
CONVENIENT PROGRAM RUNNING TIME

'''


