#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 16 00:08:23 2026

@author: nitaishah
"""


from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i , j = 0 , 1

        while i<j and j<n:
            if nums[i] == 0 and nums[j]!= 0:
                nums[i], nums[j] = nums[j], nums[i]
                i+=1
                j+=1
            elif nums[i] == 0 and nums[j] == 0:
                j+=1
            elif nums[i] != 0 and nums[j] == 0:
                i+=1
                j+=1
                
            else:
                i+=1
                j+=1
        
        return nums

nums = [0,1,0,3,12]
s = Solution()
print(s.moveZeroes(nums))