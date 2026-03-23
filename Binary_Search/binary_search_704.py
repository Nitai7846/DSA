#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 28 14:58:30 2026

@author: nitaishah
"""

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        n = len(nums)
        
        left, right = 0, n-1
        
        while left<=right:
            
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid 
            elif nums[mid] < target:
                left = mid+1
            else:
                right = mid - 1
        
        return -1 
            
        
      


S = Solution()

# Test case 1: target exists
print(S.search([-1, 0, 3, 5, 9, 12], 9))   # Expected: 4

# Test case 2: target doesn't exist
print(S.search([-1, 0, 3, 5, 9, 12], 2))   # Expected: -1

# Test case 3: single element, found
print(S.search([5], 5))                      # Expected: 0

# Test case 4: single element, not found
print(S.search([5], 3))                      # Expected: -1