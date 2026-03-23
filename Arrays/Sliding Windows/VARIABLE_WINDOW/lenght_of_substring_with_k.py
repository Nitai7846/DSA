#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 26 09:49:46 2026

@author: nitaishah
"""

from typing import List 


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        
        if k ==0:
            return 0 
        
        n = len(s)
        d = {}
        
        i = 0
        j = 0 
        
        max_len = 0 
        
        while j<n:
            
            d[s[j]] = d.get(s[j], 0) + 1
            
            while len(d) > k and i<j:
                
                d[s[i]] = d.get(s[i], 0) - 1
                if d[s[i]] == 0:
                    del d[s[i]]
            
                i+=1
                
            max_len = max(max_len, j-i+1)
            j+=1
        
        return max_len 
            
test_cases = [
    ("eceba", 2, 3),
    ("aa", 1, 2),
    ("aabacbebebe", 3, 7),
    ("abc", 0, 0),
    ("abc", 5, 3),
]

sol = Solution()

for s, k, expected in test_cases:
    result = sol.lengthOfLongestSubstringKDistinct(s, k)
    status = "PASSED" if result == expected else "FAILED"
    print(f"{status} | s={s}, k={k} | expected={expected}, got={result}")


                
                