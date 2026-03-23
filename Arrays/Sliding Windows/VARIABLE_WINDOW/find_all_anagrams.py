#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 26 19:12:17 2026

@author: nitaishah
"""



from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        if len(p) > len(s): return []
        
        pCount, sCount = {}, {}
        
        for i in range(len(p)):
            pCount[p[i]] = pCount.get(p[i], 0) + 1
            sCount[s[i]] = sCount.get(s[i], 0) + 1
        
        res = [0] if sCount == pCount else []
        l = 0 
        for r in range(len(p), len(s)):
            sCount[s[r]] = sCount.get(s[r], 0) + 1
            sCount[s[l]] -=1
            
            if sCount[s[l]] == 0:
                sCount.pop(s[l])
                
            l+=1
            
            if sCount == pCount:
                res.append(l)
        
        return res



test_cases = [
    ("cbaebabacd", "abc", [0, 6]),
    ("abab", "ab", [0, 1, 2]),
    ("af", "be", []),
    ("aa", "bb", []),
    ("aaaaaaaaaa", "aaaaaaaaaaaaa", []),
]

sol = Solution()

for s, p, expected in test_cases:
    result = sol.findAnagrams(s, p)
    status = "PASSED" if result == expected else "FAILED"
    print(f"{status} | s={s}, p={p} | expected={expected}, got={result}")
    
                    
                    
                    
                
                
                
            
        
        
            