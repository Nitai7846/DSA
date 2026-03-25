#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 00:06:21 2026

@author: nitaishah
"""

class Solution:

    def func(self, sum, last, nums, k ,ans):

        if sum == 0 and len(nums) == k:
            ans.append(list(nums))
            return 
        if sum<=0 or len(nums)>k:
            return 

        for i in range(last, 10):

            if i <= sum:

                nums.append(i)
                self.func(sum-i, i+1, nums, k, ans)
                nums.pop()
            else:
                break 

    def combinationSum3(self, k, n):
        #your code goes here

        ans = []
        nums = []
        self.func(n, 1, nums, k, ans )
        return ans 