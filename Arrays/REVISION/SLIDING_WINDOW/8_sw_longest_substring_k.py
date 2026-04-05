#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 19:12:53 2026

@author: nitaishah
"""

"""
PROBLEM: Longest Substring with At Most K Distinct Characters (LC 340)
Given a string s and integer k, find the length of the longest substring 
that contains at most k distinct characters.

TRICK: Variable sliding window using a dictionary to track character frequencies.
- Expand by adding s[j] to the dict
- Shrink from the left whenever dict has more than k keys
- Remove key entirely from dict when its count hits 0

KEY INSIGHT: This is the direct generalisation of Fruits in a Basket.
Fruits in a Basket is exactly this problem with k=2. The only difference 
is replacing the hardcoded 2 with k. Recognising this pattern saves you 
from solving it from scratch.

NUMBER OF KEYS IN DICT = NUMBER OF DISTINCT CHARACTERS IN WINDOW.
Deleting a key when count hits 0 is critical for len(d) to correctly 
reflect the number of distinct characters.

TIME: O(n) | SPACE: O(k) — dict holds at most k+1 keys at any time
"""
def longestSubstringK(s, k):
    
    n = len(s)
    i = 0 
    j = 0 
    
    max_len = 0 
    d = {}
    
    while j<n:
        
        d[s[j]] = d.get(s[j], 0) + 1
        
        while len(d) > k:
            
            d[s[i]] -= 1
            if d[s[i]] == 0:
                del d[s[i]]
            
            i+=1
        
        max_len = max(max_len, j-i+1)
        j+=1
    
    return max_len