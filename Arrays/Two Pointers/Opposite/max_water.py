#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 14 15:14:06 2026

@author: nitaishah
"""

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        n = len(height)
        max_water = 0
        i = 0

        
        for i in range(0,n):
            j = n-1
            while j>i:
                max_height = min(height[i], height[j])
                max_water = max(max_water, max_height*(j-i))
                j-=1
        
        return max_water

    def maxAreaO(self, height: List[int]) -> int:
        
        n = len(height)
        max_water = 0
        i = 0 
        j = n-1
        
        while i<j:
            
            max_height = min(height[i], height[j])
            max_water = max(max_water, max_height*(j-i))
            
            if height[i] < height[j]:
                i+=1
            
            elif height[j] > height[i]:
                j-=1
            
            else:
                i+=1
        
        return max_water
    
    
                
height = [1,8,6,2,5,4,8,3,7]
s = Solution()
s.maxAreaO(height)

height = [1,1]
s = Solution()
s.maxArea(height)