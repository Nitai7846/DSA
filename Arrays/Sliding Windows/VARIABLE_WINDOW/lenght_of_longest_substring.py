#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 21 09:50:48 2026

@author: nitaishah
"""

from typing import List

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        n = len(s)
        seen = set()
        max_len = 0
        i = 0
        j = 0 
        
        while j<n:
            
            if s[j] not in seen:
                seen.add(s[j])
                j+=1
                max_len = max(max_len, j-i)
            
            elif s[j] in seen:
                seen.remove(s[i])
                i+=1
                #seen = set()
        
        return max_len 
                
    
S = Solution()
s = "abcabcbb"
print(S.lengthOfLongestSubstring(s))

