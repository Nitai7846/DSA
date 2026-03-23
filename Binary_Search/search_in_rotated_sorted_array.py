#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 02:29:17 2026

@author: nitaishah
"""

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        
        n = len(nums)
        left = 0 
        right = n-1
        
        while left<right:
            
            mid = (left+right) // 2
            
            if nums[mid] > 
    

S = Solution()

print(S.search([4,5,6,7,0,1,2], 0))  
# Expected: 4

print(S.search([4,5,6,7,0,1,2], 3))  
# Expected: -1

print(S.search([1], 0))              
# Expected: -1

print(S.search([1], 1))              
# Expected: 0

print(S.search([3,1], 1))            
# Expected: 1

print(S.search([5,1,3], 3))          
# Expected: 2