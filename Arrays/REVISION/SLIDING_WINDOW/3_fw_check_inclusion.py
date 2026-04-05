#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 15:58:45 2026

@author: nitaishah
"""
"""
PROBLEM: Permutation in String (LC 567)
Given two strings s1 and s2, return True if any permutation/anagram 
of s1 exists as a substring of s2.

TRICK: Fixed sliding window of size len(s1) using frequency arrays of size 26.
- Build initial frequency arrays for s1 and the first window of s2
- Slide across s2, adding new right char and removing old left char
- Compare frequency arrays at each step

KEY INSIGHT: Two strings are anagrams if and only if their character 
frequency arrays are identical. Using a fixed array of size 26 (one per 
letter) is more efficient than a dictionary since input is always lowercase letters.

TIME: O(n) | SPACE: O(1) — frequency arrays are fixed size 26
"""
def checkInclusion(s1, s2):
    
    s1_len = len(s1)
    s2_len = len(s2)
    
    if s1_len > s2_len:
        return False 
    
    countss1 = [0]*26 
    countss2 = [0]*26
    
    for r in range(s1_len):
        countss1[ord(s1[r]) - 97] += 1
        countss2[ord(s2[r]) - 97] += 1
        
    if countss1 == countss2:
        return True 
    
    for r in range(s1_len, s2_len):
        countss2[ord(s2[r]) - 97] += 1
        countss2[ord(s2[r - s1_len]) - 97] -= 1
        if countss1 == countss2:
            return True
    
    return False