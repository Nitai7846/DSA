#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 15:46:47 2026

@author: nitaishah
"""

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        
        low = 0 
        high = len(nums) - 1
        
        ans = -1
        
        while low<=high:
            
            mid = (low+high) // 2
            
            if nums[mid] == target:
                return mid 
            
            if nums[low] <= nums[mid]:
                
                if target>=nums[low] and target<=nums[mid]:
                    
                    high = mid-1
                
                else:
                    
                    low = mid+1
                   
            
            elif nums[mid] <= nums[high]:
                
                if target>= nums[mid] and target <=  nums[high]:
                    
                    low = mid+1
                
                else:
                    high = mid-1 
                    
            
        return -1 
                
                               
            
    
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

print(S.search([3,1], 3))
# Expected: 0

print(S.search([5,1,3], 3))
# Expected: 2

print(S.search([5,1,3], 5))
# Expected: 0

print(S.search([6,7,1,2,3,4,5], 4))
# Expected: 5

print(S.search([6,7,1,2,3,4,5], 8))
# Expected: -1
