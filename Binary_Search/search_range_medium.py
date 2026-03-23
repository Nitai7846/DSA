#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 28 18:34:38 2026

@author: nitaishah
"""

from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def findLeft(nums, target):
            left, right = 0, len(nums) - 1
            result = -1
            
            while left <= right:
                mid = (left + right) // 2
                
                if nums[mid] == target:
                    result = mid
                    right = mid - 1   # keep going left
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            
            return result
        
        def findRight(nums, target):
            left, right = 0, len(nums) - 1
            result = -1
            
            while left <= right:
                mid = (left + right) // 2
                
                if nums[mid] == target:
                    result = mid
                    left = mid + 1    # keep going right
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            
            return result
        
        return [findLeft(nums, target), findRight(nums, target)]


S = Solution()

# Test case 1: target exists multiple times
print(S.searchRange([5, 7, 7, 8, 8, 10], 8))  # Expected: [3, 4]

# Test case 2: target exists once
print(S.searchRange([5, 7, 7, 8, 8, 10], 7))  # Expected: [1, 2]

# Test case 3: target not found
print(S.searchRange([5, 7, 7, 8, 8, 10], 6))  # Expected: [-1, -1]

# Test case 4: empty array
print(S.searchRange([], 0))                    # Expected: [-1, -1]

# Test case 5: single element found
print(S.searchRange([1], 1))                   # Expected: [0, 0]