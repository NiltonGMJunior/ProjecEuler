# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 17:25:17 2018

@author: Nilton Junior
"""

def isPalindrome(num):
    
    num_str = str(num)
    
    if len(num_str) % 2 == 0:
        num_str_first_half = num_str[ : len(num_str) // 2]
        num_str_second_half = num_str[len(num_str) // 2 : ]
    else:
        num_str_first_half = num_str[ : len(num_str) // 2]
        num_str_second_half = num_str[len(num_str) // 2 + 1 : ]
    
    return num_str_first_half == num_str_second_half[::-1]

def isLychrel(num):
    
    n = num
    
    if isPalindrome(num) == False:
        iter_left = 50
        while iter_left != 0:
            n = n + int(str(n)[::-1])
            if isPalindrome(n):
                return False
            else:
                iter_left -= 1
    else:
        return False
    
    return True

def main():
   
    lim = 10000
    counter = 0
    
    for i in range(1, lim):
        if isLychrel(i) == True:
            print(i)
            counter += isLychrel(i)
         
    
    print(counter)
    
    return

if __name__ == "__main__":
    main()