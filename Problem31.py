# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 16:12:17 2017

@author: Nilton Junior
"""

def isSumTwo(coeffs):
    
    s = 0
    base = [1, 2, 5, 10, 20, 50, 100]
    
    for i in range(len(coeffs)):
        
        s += coeffs[i]*base[i]
        
    if s == 200:
        return True
    
    return False

def main():
    
    cnt = 0
    
    for p100 in range(3):
        for p50 in range(5):
            for p20 in range(11):
                for p10 in range(21):
                    for p5 in range(41):
                        for p2 in range(101):
                            for p1 in range(201):
                                coeffs = [p1, p2, p5, p10, p20, p50, p100]
                                if isSumTwo(coeffs):
                                    print(coeffs)
                                    cnt += 1
    
    print(cnt)
    
    return

if __name__ == '__main__':
    main()