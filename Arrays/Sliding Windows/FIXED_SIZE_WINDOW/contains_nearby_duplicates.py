#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 26 11:38:54 2026

@author: nitaishah
"""

from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        visited = set()
        
        i = 0 
        j = i
        
        while j<n:
            
            if nums[j] not in visited and len(visited) <= k:
                visited.add(nums[j])
                j+=1
            
            elif nums[j] in visited and len(visited) <=k :
                return True
            
            
            elif len(visited) > k:
                visited.remove(nums[i])
                i+=1
                

        if j>=n:
            return False
            
            
       
        
        
        
            
         
            
            
            
test_cases = [
    ([1,2,3,1], 3, True),
    ([1,0,1,1], 1, True),
    ([1,2,3,1,2,3], 2, False),
    ([1], 1, False),
    ([1,1], 1, True),
]

sol = Solution()

for nums, k, expected in test_cases:
    result = sol.containsNearbyDuplicate(nums, k)
    status = "PASSED" if result == expected else "FAILED"
    print(f"{status} | nums={nums}, k={k} | expected={expected}, got={result}")
