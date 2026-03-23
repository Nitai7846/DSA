#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  8 17:59:28 2026

@author: nitaishah
"""

class Solution:
    def removeDuplicates2(self, nums):
        
        n = len(nums)
        i = 0
        
        for j in range(n):
            if i<2 or nums[j] != nums[i-2]:
                nums[i] = nums[j]
                i+=1
            print(nums)
        
        return i

   

                
                
                
s = Solution()  
nums1 = [1,1,1,2,2,3]
k1 = s.removeDuplicates2(nums1)
print(k1, nums1[:k1])

nums2 = [0,0,1,1,1,1,2,3,3]
k2 = s.removeDuplicates2(nums2)
print(k2, nums2[:k2])
