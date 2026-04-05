#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 16:39:50 2026

@author: nitaishah
"""
"""
PROBLEM: Minimum Size Subarray Sum (LC 209)
Given an array of positive integers nums and a positive integer target,
return the minimum length subarray whose sum is >= target.
Return 0 if no such subarray exists.

TRICK: Variable sliding window.
- Expand by always adding nums[j] and advancing j
- Once window sum >= target, shrink from the left recording minimum length
  at each valid state, until sum drops below target
- Initialize val_len as infinity so any valid window will update it

KEY INSIGHT: Unlike longest substring problems where you shrink one step 
and re-expand, here you keep shrinking in an inner while loop as long as 
the window is still valid — because a smaller valid window might be the answer.
Returning 0 if val_len never updated means no valid subarray was found.

NOTE: j is incremented before recording val_len, so the window length 
is j-i (not j-i+1) — same trick as longest substring without repeating characters.

TIME: O(n) — each element is added and removed at most once | SPACE: O(1)
"""
def minSubArrayLen(target, nums):
    
    n = len(nums)
    i = 0
    j = 0 
    val = 0 
    val_len = float('inf')
    
    while j<n:
        
        val += nums[j]
        j+=1
        
        while val >= target:
            
            val_len = min(val_len, j-i)
            val = val - nums[i]
            i+=1
            
        
    return 0 if val_len == float('inf') else val_len