#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 28 16:26:02 2026

@author: nitaishah
"""

# The guess API is already defined for you.
# def guess(num: int) -> int:

# -------- Mock setup for local testing --------
picked = 6

def guess(num: int) -> int:
    if num > picked:
        return -1
    elif num < picked:
        return 1
    else:
        return 0
# ----------------------------------------------

class Solution:
    def guessNumber(self, n: int) -> int:
        
        left, right = 1, n 
        
        while left<+right:
            
            mid = (left+right) // 2
            
            result = guess(mid)
            
            if result == 0:
                return mid 
            elif result == 1:
                left = mid + 1
            else:
                right = mid - 1
            


S = Solution()

# Test case 1
picked = 6
print(S.guessNumber(10))   # Expected: 6

# Test case 2
picked = 1
print(S.guessNumber(1))    # Expected: 1

# Test case 3
picked = 2
print(S.guessNumber(10))   # Expected: 2