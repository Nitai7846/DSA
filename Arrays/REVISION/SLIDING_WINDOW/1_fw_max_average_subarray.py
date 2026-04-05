#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 14:56:12 2026

@author: nitaishah
"""

"""
PROBLEM: Maximum Average Subarray I (LC 643)
Given an array nums and integer k, find the contiguous subarray 
of length k that has the maximum average, and return that average.

TRICK: Fixed sliding window of size k.
- Build the initial window sum using sum(nums[:k])
- Slide by adding the new right element and removing the old left element
- No need to recompute the entire sum each time — just adjust by one element on each side
- Divide the max sum by k only at the end

KEY INSIGHT: Since window size is fixed, maximizing the sum = maximizing the average.
So track max sum throughout, divide once at the end.

TIME: O(n) | SPACE: O(1)
"""
def findMaxAverage(nums, k):
    
    n = len(nums)
    i = 0 
    
    val = sum(nums[:k])
    max_val = val 
    
    j = k
    
    while j<n:
        
        val = val + nums[j] - nums[i]
        max_val = max(max_val, val) 
        j+=1
        i+=1
        
    return max_val/k