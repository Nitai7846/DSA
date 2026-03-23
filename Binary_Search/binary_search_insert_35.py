#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 28 15:26:59 2026

@author: nitaishah
"""

from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        n = len(nums)
        left, right = 0 , n-1
        
        while left<=right:
            
            mid = (left+right) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] <= target:
                left+=1
            elif nums[mid] >= target:
                right-=1
            
        return left
        


S = Solution()

# Test case 1: target exists
print(S.searchInsert([1, 3, 5, 6], 5))   # Expected: 2

# Test case 2: target not found, insert in middle
print(S.searchInsert([1, 3, 5, 6], 2))   # Expected: 1

# Test case 3: target smaller than all
print(S.searchInsert([1, 3, 5, 6], 0))   # Expected: 0

# Test case 4: target larger than all
print(S.searchInsert([1, 3, 5, 6], 7))   # Expected: 4

# Test case 5: single element, target not found
print(S.searchInsert([1], 2))            # Expected: 1