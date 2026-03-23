#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 23 19:42:55 2026

@author: nitaishah
"""


from typing import List 

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        n = len(fruits)
        d = {}
        
        i = 0
        j = 0
        
        max_len = 0 
        
        while j<n:
            
            
            d[fruits[j]] = d.get(fruits[j], 0) + 1

   

            
            
            while len(d) > 2 and i<j:
                
 
                d[fruits[i]]  = d.get(fruits[i], 0) - 1
                if d[fruits[i]] == 0:
                    del d[fruits[i]]
                
                i+=1
            max_len = max(max_len, j-i+1)
            j+=1
        return max_len
                
fruits =  [1,2,1]
s = Solution()
print(s.totalFruit(fruits))
