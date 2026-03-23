#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  6 22:06:52 2026

@author: nitaishah
"""

class Solution:
    def removeDuplicates(self, nums):
        
        n = len(nums)
        i = 0 
        k1 = 1
        
        for j in range(1, n):
            if nums[j] != nums[i]:
                nums[i+1] = nums[j]
                i+=1
                k1+=1
            else:
                continue
       
        
                
        return k1 

class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0

        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]

        return i + 1


s = Solution()

nums1 = [1, 1, 2]
k1 = s.removeDuplicates(nums1)
print(k1, nums1[:k1])

nums2 = [0,0,1,1,1,2,2,3,3,4]
k2 = s.removeDuplicates(nums2)
print(k2, nums2[:k2])

nums3 = [1,2,3,4,5]
k3 = s.removeDuplicates(nums3)
print(k3, nums3[:k3])

nums4 = [1,1,1,1]
k4 = s.removeDuplicates(nums4)
print(k4, nums4[:k4])

nums5 = []
k5 = s.removeDuplicates(nums5)
print(k5, nums5)
