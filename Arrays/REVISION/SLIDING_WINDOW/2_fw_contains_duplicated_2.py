#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 15:34:27 2026

@author: nitaishah
"""
"""
PROBLEM: Contains Duplicate II (LC 219)
Given an array nums and integer k, return True if there exist two indices 
i and j such that nums[i] == nums[j] and abs(i - j) <= k.

TRICK: Fixed sliding window of size k using a set.
- Maintain a window of at most k elements in a set
- If the new element already exists in the set, a duplicate within distance k is found
- If window exceeds size k, remove the leftmost element and slide forward

KEY INSIGHT: A set of size k naturally enforces the distance constraint —
if two equal elements are both in a window of size k, their indices differ by at most k.

TIME: O(n) | SPACE: O(k)
"""
def containsNearbyDuplicate(nums, k):
    
    n = len(nums)
    visited = set()
    
    i = 0 
    j = i 
    
    while j<n:
        
        if nums[j] not in visited and len(visited) <= k:
            visited.add(nums[j])
            j+=1
        
        elif nums[j] in visited and len(visited) <= k:
            return True 
        
        elif len(visited) > k: 
            visited.remove(nums[i])
            i+=1
        
        if j>=n:
            return False
        
            