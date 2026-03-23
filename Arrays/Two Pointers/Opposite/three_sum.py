#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 12 12:32:38 2026

@author: nitaishah
"""

from typing import List

class Solution:
    def threeSum(self, nums):
        
        n = len(nums)
        triplet_set = set()
        
        for i in range(n):
            hashset = set()
            for j in range(i+1, n):
                third = - (nums[i] + nums[j])
                if third in hashset:
                    temp = [nums[i], nums[j], third]
                    temp.sort()
                    triplet_set.add(tuple(temp))
                    
                hashset.add(nums[j])
                
        
        ans = [list(triplet) for triplet in triplet_set]
        return ans
                
                    
  
    def threeSum(self, nums):
        nums.sort()
        result = []
        n = len(nums)
        
        for i in range(n - 2):
            # Skip duplicates for i
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            j = i + 1
            k = n - 1
            
            while j < k:  # Fixed condition
                total = nums[i] + nums[j] + nums[k]
                
                if total == 0:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    # Skip duplicates for j and k
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1
                elif total < 0:
                    j += 1
                else:
                    k -= 1
        
        return result 
        
        


s = Solution()

nums1 = [-1, 0, 1, 2, -1, -4]
print(s.threeSumO(nums1))  # [[-1,-1,2],[-1,0,1]] (order may vary)

nums2 = [0, 0, 0, 0]
print(s.threeSum(nums2))  # [[0,0,0]]

nums3 = [1, 2, 3, 4]
print(s.threeSum(nums3))  # []

nums4 = [-2, 0, 1, 1, 2]
print(s.threeSum(nums4))  # [[-2,0,2],[-2,1,1]] (order may vary)

nums5 = []
print(s.threeSum(nums5))  # []
