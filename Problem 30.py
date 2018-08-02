# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 18:23:48 2017

@author: Nilton Junior
"""

# Finding search limit

t = lambda n : n * 9**5

n = 1

tf = True

while tf:
    nines = '9';
    while len(nines) < n:
        nines += '9'
    tf = not(int(nines) > t(n))
    n = n + 1

# nines is the limit
    
limit = int(nines)

sum = 0


def sum_fifth(n):
    