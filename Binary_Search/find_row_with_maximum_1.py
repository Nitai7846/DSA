#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 19:09:30 2026

@author: nitaishah
"""

class Solution:

    def lowerBound(self, arr, n, x):

        low = 0
        high = n-1
        result = n 
        while low<=high:

            mid = (low+high) // 2
            if arr[mid] >= x:
                result = mid 
                high = mid - 1

            else:
                low = mid+1

        return result  

    def rowWithMax1s(self, mat):

        cnt_max = 0 
        index = -1
        n, m = len(mat), len(mat[0])

        for i in range(n):

            cnt_ones = m - self.lowerBound(mat[i], m , 1)

            if cnt_ones > cnt_max:
                cnt_max = cnt_ones
                index = i 
        
        return index  