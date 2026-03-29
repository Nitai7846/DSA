#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 10:47:38 2026

@author: nitaishah
"""

class Solution:

    def __init__(self):
        self.result = []
    
    def path(self, m, x, y, dir, n):
        if x == n-1 and y ==n-1:
            self.result.append(dir)
            return 
        
        if m[x][y] == 0:
            return 
        
        m[x][y] = 0

        if x>0:
            self.path(m, x-1, y, dir + 'U', n)
        
        if y>0:
            self.path(m, x, y-1, dir + 'L', n)
        
        if x<n-1:
            self.path(m, x+1, y, dir + 'D', n)
        
        if y<n-1:
            self.path(m, x, y+1, dir + 'R', n)
        
        m[x][y] = 1 
        
    def findPath(self, grid):
        #your code goes here

        n = len(grid)
        self.result = []

        if grid[0][0] == 0 or grid[n-1][n-1] == 0:
            return self.result
        
        self.path(grid, 0, 0, "", n)

        self.result.sort()

        return self.result 