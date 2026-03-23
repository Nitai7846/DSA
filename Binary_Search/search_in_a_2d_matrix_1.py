#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 00:31:33 2026

@author: nitaishah
"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])

        low, high = 0 , n*m - 1

        while low <= high:
            mid = (low+high)//2

            row = mid // m 
            col = mid % m 

            if matrix[row][col] == target:
                return True 
            elif matrix[row][col] < target:
                low = mid + 1
            else:
                high = mid - 1
        
        return False 