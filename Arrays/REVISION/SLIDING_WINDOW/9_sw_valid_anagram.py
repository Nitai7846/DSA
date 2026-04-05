#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 00:02:46 2026

@author: nitaishah
"""

"""
PROBLEM: Find All Anagrams in a String (LC 438)
Given strings s and p, return a list of all starting indices in s 
where an anagram of p begins.

TRICK: Fixed sliding window of size len(p) using two frequency dictionaries.
- Build initial frequency counts for all of p and the first window of s
- Slide across s, adding new right char and removing old left char
- Collect starting index l whenever window frequencies match p's frequencies

KEY INSIGHT: Same core idea as Permutation in String (LC 567) — 
two strings are anagrams if their frequency dicts are identical.
The difference is instead of returning True on first match, 
you collect all matching starting indices.

IMPORTANT: When a match is found, append l (not r) because l is the 
start of the current window. r is the end.

INITIAL WINDOW CHECK: res = [0] if sCount == pCount else [] handles 
the first window before sliding begins, so the loop can start at len(p).

NOTE: Uses dict instead of fixed array of 26 because dict deletion 
keeps comparisons clean — a key with count 0 would cause a false 
mismatch against pCount which has no such key.

TIME: O(n) | SPACE: O(1) — dicts hold at most 26 keys
"""
def findAnagrams(s, p):
    
    if len(p) > len(s):
        return []
    
    pCount, sCount = {}, {}
    
    for i in range(len(p)):
        pCount[p[i]] = pCount.get(p[i], 0)+1
        sCount[s[i]] = sCount.get(s[i], 0)+1
        
    res = [0] if sCount == pCount else []        
    
    l = 0
    for r in range(len(p), len(s)):
        sCount[s[r]] = sCount.get(s[r], 0) + 1
        sCount[s[l]] -= 1 
        
        if sCount[s[l]] == 0:
            sCount.pop(s[l])
        
        l+=1
        
        if sCount == pCount:
            res.append(l)
    
    return res