#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 13 23:10:18 2026

@author: nitaishah
"""


from typing import List 
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        
        n = len(nums)
        nums.sort()
        count = 0
        for k in range(2,n):
            i, j = 0, k-1
            
            while i<j:
                
                if nums[i] + nums[j] > nums[k]:
                    count += (j-i)
                    j -=1
                else:
                    i+=1
        
        return count 
    
    
    
    
                
                
            
            
        
        