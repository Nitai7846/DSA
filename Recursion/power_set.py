#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 18:28:08 2026

@author: nitaishah
"""

from typing import List 

class Solution:
    
    def subsets(self, nums:List[int])  -> List[List[int]]:
        result = []
        
        def backtrack(index, current):
            if index == len(nums):
                result.append(current[:])
                return 
            
            current.append(nums[index])
            backtrack(index+1, current)
            
            current.pop()
            backtrack(index+1, current)
            
        backtrack(0, [])
        
        
            
            
    