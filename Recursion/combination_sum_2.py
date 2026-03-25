#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 22:24:49 2026

@author: nitaishah
"""

class Solution:
    def __init__(self):
        self.ans = []
    
    def func(self, ind, sum, nums, candidates):
        if sum == 0:
            self.ans.append(nums[:])
            return
        
        if ind == len(candidates) or candidates[ind] > sum:  # fixed
            return
        
        # include
        nums.append(candidates[ind])
        self.func(ind + 1, sum - candidates[ind], nums, candidates)
        nums.pop()
        
        # skip duplicates
        for i in range(ind + 1, len(candidates)):
            if candidates[i] != candidates[ind]:
                self.func(i, sum, nums, candidates)
                break
    
    def combinationSum2(self, candidates, target):
        candidates.sort()
        self.ans = []
        self.func(0, target, [], candidates)
        return self.ans