#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  6 23:13:50 2026

@author: nitaishah
"""

class Solution:
    def moveZeroes(self, nums):
        
        n = len(nums)
        
        slow = 0
        
        for fast in range(len(nums)):
            if nums[fast]!=0:
                nums[slow] = nums[fast]
                slow += 1
                print(nums)
            
                
                
        for i in range(slow, len(nums)):
            nums[i] = 0 
            
                




s = Solution()

nums1 = [0,1,0,3,0,2]
s.moveZeroes(nums1)
print(nums1)

nums2 = [0,0,0,1]
s.moveZeroes(nums2)
print(nums2)

nums3 = [1,2,3,4]
s.moveZeroes(nums3)
print(nums3)

nums4 = [0,0,0,0]
s.moveZeroes(nums4)
print(nums4)

nums5 = []
s.moveZeroes(nums5)
print(nums5)

