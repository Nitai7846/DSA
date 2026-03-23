#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 21 11:19:38 2026

@author: nitaishah
"""

from typing import List

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        longest = 0
        l = 0 
        counts = [0] * 26 
        
        for r in range(len(s)):
            counts[ord(s[r]) - 65] +=1 
            
            while (r-l+1) - max(counts) > k :
                counts[ord(s[l]) - 65] -=1 
                l+=1
            
            
            longest = max(longest, (r-l+1))
            
            
                
            
        
       
           
                