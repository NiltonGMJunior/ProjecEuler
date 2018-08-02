# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 13:50:18 2017

@author: Nilton Junior
"""

def factorial(n):
    
    f = 1
    for i in range(n):
        f *= i + 1
    
    return f

def findN():
    
    n = 1
    
    while n*factorial(9) > 10**n - 1:
        n += 1
    
    return n

def main():
    
    
    
    print(findN())
    
    return

if __name__ == "__main__":
    main()