#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 15 23:41:53 2026

@author: nitaishah
"""

from typing import List

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        i = 0 
        j = n -1 

        while i<j:
            if nums[i] % 2 == 1 and nums[j] % 2 == 0:
                nums[i], nums[j] = nums[j], nums[i]
                i+=1
                j-=1
            elif nums[i] % 2 == 1:
                j-=1
            else:
                i+=1

        return nums 



nums = [0,1,2]

s = Solution()
print(s.sortArrayByParity(nums))
