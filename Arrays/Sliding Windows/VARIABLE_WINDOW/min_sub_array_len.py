#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 20 17:07:41 2026

@author: nitaishah
"""

from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        n = len(nums)
        i = 0
        j = i 
        val = 0
        val_len = float('inf')
        
        while j<n:
            val += nums[j]
            j+=1
            
            while val >= target:
                val_len = min(val_len, j-i)
                val-=nums[i]
                i+=1
        
        return 0 if val_len == float('inf') else val_len
        
        
target = 7
nums = [2,3,1,2,4,3]

s = Solution()
print(s.minSubArrayLen(target, nums))
