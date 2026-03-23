#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 01:28:52 2026

@author: nitaishah
"""



class Solution:
    def findMin(self, nums: list[int]) -> int:
        
        n = len(nums)
        left = 0 
        right = n-1
        
        while left< right:
            
            mid = (left+right) // 2
            
            if nums[mid] > nums[right]:
                left = mid+1
                
            elif nums[mid]<nums[right]:
                right = mid
        
        return nums[left]

class Solution:
    """ Function to find minimum element
        in a rotated sorted array """
    def findMin(self, arr):
        # Initialize low and high indices
        low, high = 0, len(arr) - 1
        
        # Initialize ans to maximum integer value
        ans = float('inf')
        while low <= high:
            mid = (low + high) // 2
            
            # Check if left part is sorted
            if arr[low] <= arr[mid]:
                """ Update ans with minimum 
                    of ans and arr[low] """
                ans = min(ans, arr[low])
                
                # Move to the right part
                low = mid + 1
            else:
                """ Update ans with minimum 
                    of ans and arr[mid] """
                ans = min(ans, arr[mid])
                
                # Move to the left part
                high = mid - 1
        
        # Return the minimum element found
        return ans

if __name__ == "__main__":
    arr = [4, 5, 6, 7, 0, 1, 2, 3]
    
    #Create an instance of the Solution class
    sol = Solution()
    
    ans = sol.findMin(arr)
    
    print("The minimum element is:", ans)

    
    
S = Solution()

print(S.findMin([3,4,5,1,2]))     
# Expected: 1

print(S.findMin([4,5,6,7,0,1,2])) 
# Expected: 0

print(S.findMin([11,13,15,17]))   
# Expected: 11

print(S.findMin([2,1]))           
# Expected: 1

print(S.findMin([5,1,2,3,4]))     
# Expected: 1

print(S.findMin([1]))             
# Expected: 1

print(S.findMin([2,3,4,5,6,7,1])) 
# Expected: 1
