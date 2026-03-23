#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 12 12:26:35 2026

@author: nitaishah
"""

class Solution:
    def twoSum(self, nums, target):
        
        n = len(nums) 
        i = 0
        j = n-1
        
        while i < n:
            val = nums[i] + nums[j]
            if val < target:
                i+=1
            elif val > target:
                j-=1 
            else:
                return i, j
        
        
        



s = Solution()

numbers1 = [2, 7, 11, 15]
target1 = 9
print(s.twoSum(numbers1, target1))  # [1, 2]

numbers2 = [2, 3, 4]
target2 = 6
print(s.twoSum(numbers2, target2))  # [1, 3]

numbers3 = [-1, 0]
target3 = -1
print(s.twoSum(numbers3, target3))  # [1, 2]

numbers4 = [1, 2, 3, 4, 5]
target4 = 100
print(s.twoSum(numbers4, target4))  # [-1, -1] (if no solution)
