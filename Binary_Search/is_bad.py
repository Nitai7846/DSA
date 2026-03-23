#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 28 18:00:45 2026

@author: nitaishah
"""

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

# -------- Mock setup for local testing --------
bad = 4

def isBadVersion(version: int) -> bool:
    return version >= bad
# ----------------------------------------------

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        left = 1
        right = n
        result = -1  # ⬅️ add this
        
        while left <= right:
            mid = (left + right) // 2
            is_bad = isBadVersion(mid)
            
            if is_bad == False:
                # your code here
                left = mid+1
            else:
                # your code here
                result  = mid 
                right = mid - 1
                
        
        return result
            


S = Solution()

# Test case 1
bad = 4
print(S.firstBadVersion(5))    # Expected: 4

# Test case 2
bad = 1
print(S.firstBadVersion(1))    # Expected: 1

# Test case 3
bad = 1
print(S.firstBadVersion(10))   # Expected: 1

# Test case 4
bad = 6
print(S.firstBadVersion(10))   # Expected: 6
