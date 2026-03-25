#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 22:17:54 2026

@author: nitaishah
"""

class Solution:
    def combinationSum(self, candidates, target):
        #your code goes here

        result = []

        def backtrack(index, remaining, current):
            if remaining == 0:
                result.append(current[:])
                return 
            if remaining < 0:
                return 
            
            for i in range(index, len(candidates)):
                current.append(candidates[i])
                backtrack(i,remaining-candidates[i], current)
                current.pop()
        
        backtrack(0, target, [])
        return result 