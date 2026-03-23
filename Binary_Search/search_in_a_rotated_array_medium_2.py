#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 17:07:35 2026

@author: nitaishah
"""

class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        
        
        low, high = 0, len(nums)-1
        ans = False
        
        while low<=high:
            
            mid = (low+high) // 2
            
            if nums[mid] == target:
                return True
            
            if (nums[low] == nums[mid] == nums[high]):
                low = low+1
                high = high-1
                continue 
            
            if nums[low] <= nums[mid]:
                
                if nums[low] <= target <= nums[mid]:
                    
                    high = mid-1
                
                else:
                    
                    low = mid+1
                
            elif nums[mid] <= nums[high]:
                
                if nums[mid] <= target <= nums[high]:
                    
                    low = mid+1 
                
                else:
                    
                    high = mid-1 
                    
        return ans 
        
        
        
    
S = Solution()

print(S.search([2,5,6,0,0,1,2], 0))
# Expected: True

print(S.search([2,5,6,0,0,1,2], 3))
# Expected: False

print(S.search([1,0,1,1,1], 0))
# Expected: True

print(S.search([1,1,1,1,1], 2))
# Expected: False

print(S.search([1,3,1,1,1], 3))
# Expected: True

print(S.search([3,1,1], 3))
# Expected: True

print(S.search([3,1,1], 2))
# Expected: False

print(S.search([1], 1))
# Expected: True

print(S.search([1], 0))
# Expected: False
