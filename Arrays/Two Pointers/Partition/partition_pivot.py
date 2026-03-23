#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 16 18:05:02 2026

@author: nitaishah
"""

from typing import List 

class Solution:
    def pivotArrayold(self, nums: List[int], pivot: int) -> List[int]:
        
        n = len(nums)
        pl = []
        pr = []
        pc = 0
        
        for i in range(0,n):
            if nums[i] < pivot:
                pl.append(nums[i])
            elif nums[i] > pivot:
                pr.append(nums[i])
            else:
                pc+=1
        
        print(pl)
        print(pr)
        print(pc)
        
        for i in range(0, len(pl)):
            nums[i] = pl[i]
        

        for i in range(len(pl), len(pl)+ pc):
            nums[i] = pivot
        
        j = 0
        for i in range(len(pl)+pc, n):
            nums[i] = pr[j]
            j+=1
     
            
        return nums
            

s = Solution()
nums = [9,12,5,10,14,3,10]
pivot = 10
print(s.pivotArrayold(nums, pivot))


            