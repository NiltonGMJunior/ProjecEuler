# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 13:15:56 2017

@author: Nilton Junior
"""
import time

def fib(n):
    return fib(n - 1) + fib(n - 2) if n > 2 else 1

def cached_exec(n, cache = {}):
    if n not in cache:
        cache[n] =  fib(n)
    return cache[n], cache

if __name__ == "__main__":
    cache = {}
    n = 1
    while True:
        start_time = time.time()
        fibo, cache = cached_exec(n)
        print('Fib({}) = {}. Time = {}'.format(n, fibo, float(time.time()-start_time)))
        n += 1
        if n == 100:
            break
