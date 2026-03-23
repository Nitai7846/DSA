#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 00:17:56 2026

@author: nitaishah
"""

class Solution:
    
    def canWePlace(self, nums, dist, cows):
        
        n  = len(nums)
        cntCows = 1
        
        last = nums[0]
        for i in range(1,n):
            
            if nums[i] - last >= dist:
                cntCows += 1
                last = nums[i]
            
            if cntCows >= cows:
                return True 
        
        return False 
    
    
    def aggressiveCows(self, nums, k):
        
        n = len(nums)
        low = 1
        high = nums[n-1] - nums[0]
        
        while low <= high:
            
            mid = (low+high) // 2
            
            if self.canWePlace(nums, mid, k):
                low = mid + 1
            else:
                high = mid - 1
        
        return high 

if __name__ == "__main__":
    nums = [0, 3, 4, 7, 10, 9]
    k = 4
    
    # Create an instance of the Solution class
    sol = Solution()
    
    ans = sol.aggressiveCows(nums, k)
    
    # Output the result
    print("The maximum possible minimum distance is:", ans)
