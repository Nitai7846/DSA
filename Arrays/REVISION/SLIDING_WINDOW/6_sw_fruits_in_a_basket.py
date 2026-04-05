#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 18:00:59 2026

@author: nitaishah
"""
"""
PROBLEM: Fruit Into Baskets (LC 904)
Given an array of fruits where each element is a fruit type, you have 
two baskets each holding only one type of fruit. Find the maximum number 
of fruits you can pick from a contiguous subarray using both baskets.

TRICK: Variable sliding window using a dictionary to track fruit frequencies.
- This is exactly "longest subarray with at most 2 distinct elements"
- Expand by adding fruits[j] to the dict
- Shrink from the left whenever dict has more than 2 keys
- Remove key entirely from dict when its count hits 0

KEY INSIGHT: Using a dictionary instead of a fixed array because fruit 
types can be any integer, not just letters. The number of keys in the 
dict = number of distinct fruits in the window. Deleting a key when 
count hits 0 is critical — otherwise len(d) would never decrease.

GENERALISATION: This is a special case of "longest substring with at 
most k distinct characters" with k=2. Just replace 2 with k for the 
general solution.

TIME: O(n) | SPACE: O(1) — dict holds at most 3 keys at any time
"""
def totalFruit(fruits):
    
    n = len(fruits)
    d = {}
    
    i = 0
    j = 0
    max_len = 0 
    
    while j<n:
        
        d[fruits[j]] = d.get(fruits[j], 0) + 1
        
        while len(d)>2:
            
            d[fruits[i]] -= 1
            if d[fruits[i]] == 0:
                del d[fruits[i]]
            
            i+=1
        
        max_len = max(max_len, j-i+1)
        j+=1
        
    return max_len