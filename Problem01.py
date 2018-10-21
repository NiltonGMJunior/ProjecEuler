# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 13:15:56 2017

@author: Nilton Junior
"""

n = 1000 # Limite da sequência

def sum_k(n, k):
    return k*(n//k)*(n//k + 1)//2

def euler(n):
    return sum_k(n - 1, 3) + sum_k(n - 1, 5) - sum_k(n - 1, 15)

if __name__ == "__main__":
    print(euler(n - 1))
