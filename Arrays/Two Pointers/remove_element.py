#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  8 13:11:29 2026

@author: nitaishah
"""

class Solution:
    def removeElement(self, nums, val):
        
        
        n = len(nums)
        slow = 0
        
        for fast in range(n):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
        
        return slow
            
                
            
            
                
s = Solution()

nums1 = [3,2,2,3]
k1 = s.removeElement(nums1, 3)
print(k1, nums1[:k1])

nums2 = [0,1,2,2,3,0,4,2]
k2 = s.removeElement(nums2, 2)
print(k2, nums2[:k2])

nums3 = [1,1,1]
k3 = s.removeElement(nums3, 1)
print(k3, nums3[:k3])

nums4 = [1,2,3]
k4 = s.removeElement(nums4, 4)
print(k4, nums4[:k4])

nums5 = []
k5 = s.removeElement(nums5, 0)
print(k5, nums5)
