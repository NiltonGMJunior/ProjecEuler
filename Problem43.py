# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 08:47:49 2017

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

def primeSearch(n):
    
    if n == 1:
        return 2
    
    if n == 2:
        return 3
    
    p = 3
    cnt = 2
    
    while cnt < n:
        p += 2
        if isPrime(n):
            cnt += 1
    
    return p

def panProp(s):
    
    last_digit_pos = 4
    n = 1
    
    while last_digit_pos <= len(s):
        prod = int(s[last_digit_pos - 2])*int(s[last_digit_pos - 1])*int(s[last_digit_pos])
        if prod % primeSearch(n) != 0:
            return False
        n += 1
        last_digit_pos += 1
                
    return True
    

def isPandigital(s, l):
    
    ref = list(range(l + 1))
    
    for i in ref:
        i = str(i)
    
    for i in s:
        try:
            ind = ref.index(i)
            ref = ref[:ind] + ref[ind + 1:]
        except ValueError:
            pass

    return ref == []

def main():
    
    pan_span = 9
    lower_limit = 10**(pan_span - 1)
    upper_limit = (pan_span + 1)*10**pan_span
    
    sum = 0
    
    for i in range(lower_limit, upper_limit):
        str_i = str(i)
        while len(str_i) < pan_span:
            str_i = '0' + str_i
        
        if isPandigital(str_i, pan_span):
            if panProp(str_i):
                sum += int(str_i)
        
    return sum


if __name__ == "__main__":
    main()