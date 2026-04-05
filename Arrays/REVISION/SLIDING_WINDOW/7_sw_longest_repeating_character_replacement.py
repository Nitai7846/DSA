#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 18:26:07 2026

@author: nitaishah
"""

"""
PROBLEM: Longest Repeating Character Replacement (LC 424)
Given a string s and integer k, you can replace at most k characters 
in the string. Find the length of the longest substring where all 
characters are the same after performing at most k replacements.

TRICK: Variable sliding window using a dictionary to track character frequencies.
- At any window, replacements needed = window_len - max_freq
  (total characters minus the most frequent one)
- If replacements needed <= k, window is valid
- If replacements needed > k, shrink from the left

KEY INSIGHT: You don't need to try every possible target character.
Just track the most frequent character in the current window using 
max(d.values()) — that's always the one worth keeping, replacing everything else.

IMPORTANT: max_freq and window_len must be recalculated inside the 
shrink loop, otherwise the while condition never updates and you either 
exit too early or loop forever.

TIME: O(26n) = O(n) — max(d.values()) scans at most 26 keys
SPACE: O(26) = O(1)
"""
def characterReplacement(s, k):
    
    n = len(s)
    d = {}
    
    i = 0 
    j = 0
    max_len = 0 
    
    while j<n:
        
        d[s[j]] = d.get(s[j], 0) + 1
        
        max_freq = max(d.values()) 
        window_len = j-i+1
        
        while window_len - max_freq > k:
            d[s[i]] -= 1
            if d[s[i]] == 0:
                del d[s[i]]
            i+=1
            max_freq = max(d.values())
            window_len = j-i+1
        
        max_len = max(max_len, window_len)
        j+=1
    
    return max_len