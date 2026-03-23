#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 16 00:34:36 2026

@author: nitaishah
"""


from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)
        low = 0 
        mid = 0 
        high = n - 1
        
        while mid <= high:
            
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid +=1
            
            elif nums[mid] == 1:
                mid+=1
            
            elif nums[mid] == 2:
                nums[mid], nums[high] = nums[high], nums[mid]
                high-=1
        
        return nums
    
    
nums = [2,0,2,1,1,0]
s = Solution()
print(s.sortColors(nums))
                
                
                
        