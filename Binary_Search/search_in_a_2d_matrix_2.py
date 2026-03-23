#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 00:31:59 2026

@author: nitaishah
"""

class Solution:
    def searchMatrix(self, matrix, target):

        n,m = len(matrix) , len(matrix[0])

        row, col = 0, m-1

        while row < n and col >= 0 :

            if matrix[row][col] == target:
                return True
            
            elif matrix[row][col] > target:
                col = col - 1
            
            elif matrix[row][col] < target:
                row = row + 1
        
        return False 


