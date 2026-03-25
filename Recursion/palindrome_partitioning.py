#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 00:17:28 2026

@author: nitaishah
"""

class Solution:
    def partition(self, s: str):
        def dfs(index, path):
            if index == len(s):
                res.append(path[:])
                return 
            
            for i in range(index, len(s)):

                if isPalindrome(index,i):
                    path.append(s[index:i+1])
                    dfs(i+1, path)
                    path.pop()
        
        def isPalindrome(start, end):

            while start<=end:
                if s[start] != s[end]:
                    return False
                start+=1
                end -=1 
            return True 
        
        res = []
        dfs(0, [])
        return res 