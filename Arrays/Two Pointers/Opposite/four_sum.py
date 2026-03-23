#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 13 19:54:52 2026

@author: nitaishah
"""

from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        
        n = len(nums)
        nums.sort()
        ans = []
        for i in range(0,n-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue 
            for j in range(i+1, n-2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                
                k = j+1
                l = n-1
                
                
                while k<l:
                    
                    value = nums[i] + nums[j] + nums[k] + nums[l]
                    
                    if value == target:
                        temp = [nums[i], nums[j], nums[k], nums[l]]
                        ans.append(temp)
                        
                        
                        k+=1
                        l-=1
                        
                        while k<l and nums[k] == nums[k-1]:
                            k+=1
                        while k<l and nums[l] == nums[l+1]:
                            l-=1
                            
                    
                    elif value<target:
                        k+=1
                    
                    elif value>target:
                        l-=1
        return ans 
    
s = Solution() 
nums= [-2,-1,-1,1,1,2,2] 
target=0

print(s.fourSum(nums,target))
                    
                        
                        
                    
            
        