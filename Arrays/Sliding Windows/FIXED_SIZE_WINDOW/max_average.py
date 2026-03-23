#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 26 10:26:20 2026

@author: nitaishah
"""


from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        j = k
        n = len(nums)
        val = sum(nums[:k])
        max_val = val 
        
        
        while j<n:
            
            val = val + nums[j] - nums[j-k]
            max_val = max(max_val, val)
            j+=1
        
        
        return max_val/k
                
                
                
                
                
                
            
        
       
        
       
        
 
            
            
            
            
            
                
                
                
                
                
            
            
        
        
    

test_cases = [
    ([1,12,-5,-6,50,3], 4, 12.75),
    ([5], 1, 5.0),
    ([0,1,1,3,3], 4, 2.0),
    ([4,0,4,3,3], 5, 2.8),
    ([-1,-12,-5,-6,50,3], 4, 10.5),
]

sol = Solution()

for nums, k, expected in test_cases:
    result = sol.findMaxAverage(nums, k)
    status = "PASSED" if result == expected else "FAILED"
    print(f"{status} | nums={nums}, k={k} | expected={expected}, got={result}")
