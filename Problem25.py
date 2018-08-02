# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 15:53:37 2017

@author: Nilton Junior
"""

def fib(n):
    
    if n <= 2:
        return 1
    
    f_old = 1
    f = 2
    
    for i in range(3, n):
        temp = f
        f = f_old + f
        f_old = temp
    
    return f

def main():
    
    num_digits = 0
    n = 1
    lim = 1000
    
    while num_digits < lim:
        n = n + 1
        num_digits = len(str(fib(n)))
        
    print(fib(n))
    print(n)
    
    return

if __name__ == '__main__':
    main()
    