#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 14 16:10:18 2026

@author: nitaishah
"""

from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        
        n = len(height)
        i = 0 
        j = n-1
        
        max_left = height[i]
        max_right = height[j]
        
        water = 0 
        
        while i<j:
            
            if max_left <= max_right:
                water += max_left - height[i]
                i+=1
                max_left = max(max_left, height[i])
            
            elif max_right < max_left:
                water += max_right - height[j]
                j-=1
                max_right = max(max_right, height[j])
                
            
                
            
        return water 
    
    
height = [0,1,0,2,1,0,1,3,2,1,2,1]
s = Solution()
s.trap(height)