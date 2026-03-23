#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 22 11:06:22 2026

@author: nitaishah
"""

from typing import List

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        s1_len = len(s1)
        s2_len = len(s2)
        
        if s1_len > s2_len:
            return False
        
        countss1 = [0]*26
        countss2 = [0]*26 
        
        for r in range(s1_len):
            countss1[ord(s1[r]) - 97] +=1 
            countss2[ord(s2[r]) - 97] +=1
            
        if countss1 == countss2:
            return True
        
        for r in range(s1_len, s2_len):
            countss2[ord(s2[r]) - 97] +=1
            countss2[ord(s2[r-s1_len]) - 97] -=1
            
            if countss1 == countss2:
                return True 
            
        return False
        
        
S = Solution()
s1 = "ab" 
s2 = "eidbaooo"    

print(S.checkInclusion(s1, s2))      
                
                

        
        