#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 28 16:34:21 2026

@author: nitaishah
"""



class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        
        while left<=right:
            
            mid = (left+right) // 2
            
            if mid*mid == x:
                return mid 
            elif mid*mid > x:
                right = mid-1
            elif mid*mid <x:
                result = mid
                left = mid+1
            
        return result
        
        
        


S = Solution()

# Test case 1: perfect square
print(S.mySqrt(4))    # Expected: 2

# Test case 2: not a perfect square, round down
print(S.mySqrt(8))    # Expected: 2  (2.82... → 2)

# Test case 3
print(S.mySqrt(9))    # Expected: 3

# Test case 4: zero
print(S.mySqrt(0))    # Expected: 0

# Test case 5: one
print(S.mySqrt(1))    # Expected: 1