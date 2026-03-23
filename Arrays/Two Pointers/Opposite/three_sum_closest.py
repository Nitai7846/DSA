#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 13 18:33:54 2026

@author: nitaishah
"""

from typing import List
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        n = len(nums)
        closest_sum = float('inf')
        
        for i in range(n-2):
            
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            j = i+1
            k = n-1
            
            while j<k:
                
                current_sum = nums[i] + nums[j] + nums[k]
                if abs(current_sum-target)<abs(closest_sum-target):
                    closest_sum = current_sum
            
                if current_sum == target:
                    return current_sum
                
                elif current_sum < target:
                    j+=1
                else:
                    k-=1 
            
        return closest_sum 
                    
  
        
    

s = Solution()

nums1 = [-1,2,1,-4]
target = 1
print(s.threeSumClosest(nums1,target ))  # [[-1,-1,2],[-1,0,1]] (order may vary)
