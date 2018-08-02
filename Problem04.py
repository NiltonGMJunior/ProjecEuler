# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 13:15:56 2017

@author: Nilton Junior
"""
def isPalindrome(s):
    
    l = int(len(s))
    
    tf = False
    
    if l % 2 == 0:
        
        s1 = s[0:l//2]
        
        s2 = s[l//2:l + 1][::-1]
        
        if s1 == s2:
            
            tf = True
            
    elif l == 1:
        
        tf = True
        
    else:
        
        s1 = s[0:(l - 1)//2]
        
        s2 = s[(l + 1)//2:l + 1][::-1]
        
        if s1 == s2:
            
            tf = True
            
    return tf

ref = 0

#i_ref = 0
#
#j_ref = 0
        
for i in range(100,1000):
    
    for j in range (100,1000):
        
        p_num = i*j
        
        p_str = str(p_num)
        
        if  (   isPalindrome(p_str) == True
            and p_num > ref    
            ):
            
            ref = p_num
            
#            i_ref = i
#            
#            j_ref = j
            
print(ref)

#print(i_ref)
#
#print(j_ref)

                
                
        
        
    

            



                            
            

    