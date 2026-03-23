#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 12 00:07:43 2026

@author: nitaishah
"""

class Solution:
    def pivotArray(self, nums, pivot):
        
        i, j = 0, len(nums)-1
        i2, j2 = 0, len(nums) -1 
        
        res = [0]*len(nums)

        while i<len(nums):
            
            if nums[i] < pivot:
                
                res[i2] = nums[i]
                i2+=1
            if nums[j] > pivot:
                res[j2] = nums[j]
                j2-=1
            
            i, j = i+1, j-1
        
        while i2 <= j2:
            res[i2] = res[j2] = pivot
            i2, j2 = i2+1, j2-1
            
        return res
    
class Solution:
    def pivotArray(self, nums, pivot):
        n = len(nums)
        
        # First pass: count
        less_count = 0
        equal_count = 0
        
        for num in nums:
            if num < pivot:
                less_count += 1
            elif num == pivot:
                equal_count += 1
        
        # Second pass: overwrite in-place
        i = 0
        
        # Write < pivot
        for num in nums:
            if num < pivot:
                nums[i] = num
                i += 1
        
        # Write == pivot
        for _ in range(equal_count):
            nums[i] = pivot
            i += 1
        
        # Write > pivot
        for num in nums:
            if num > pivot:
                nums[i] = num
                i += 1
        
        return nums

                
s = Solution()

nums1 = [9,12,5,10,14,3,10]
print(s.pivotArray(nums1, 10))

nums2 = [-3,4,3,2]
print(s.pivotArray(nums2, 2))

nums3 = [1,2,3]
print(s.pivotArray(nums3, 2))

nums4 = [2,2,2]
print(s.pivotArray(nums4, 2))
