#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 16:10:33 2026

@author: nitaishah
"""

"""
PROBLEM: Longest Substring Without Repeating Characters (LC 3)
Given a string s, find the length of the longest substring 
that contains no repeating characters.

TRICK: Variable sliding window using a set.
- Expand by adding s[j] when it's not in the window
- Shrink by removing s[i] from the left when a duplicate is found
- Keep shrinking until the duplicate is removed, then expand again

KEY INSIGHT: Instead of checking all substrings, maintain a window 
that is always valid (no duplicates). When a duplicate is found, 
don't reset — just shrink from the left one step at a time until 
the duplicate is gone. This avoids redundant work.

NOTE: max_len is updated as j-i (not j-i+1) because j is incremented 
before the max calculation, so it naturally accounts for the +1.

TIME: O(n) | SPACE: O(n)
"""
def lenghtOfLongestSubstring(s):
    
    n = len(s)
    seen = set()
    
    i = 0
    j = 0 
    max_len = 0
    
    while j<n:
        
        if s[j] not in seen:
            seen.add(s[j])
            j+=1
            max_len = max(max_len , j-i)
        
        else:
            seen.remove(s[i])
            i+=1
            
        
    return max_len