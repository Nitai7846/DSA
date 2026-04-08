#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 22:20:15 2026

@author: nitaishah
"""

# Question: Odd Even Linked List (LC 328)
#           Rearrange a linked list so all odd-indexed nodes come before
#           all even-indexed nodes (1-indexed). Must do it in-place.
#
# Trick: Use two pointers — one for the odd chain, one for the even chain.
#        Save the head of the even chain (firstEven) before the loop.
#        Alternate-advance both pointers, then stitch odd tail → firstEven at the end.

class ListNode:
    def __init__(self, x=0, next=None):
        self.data = x
        self.next = next

class Solution:
    
    def oddEvenList(self, head):
        if not head or not head.next:
            return head 
        
        odd = head
        even = head.next
        firstEven = head.next
        
        
        while even and even.next:
            odd.next = odd.next.next
            even.next = even.next.next
            odd = odd.next
            even = even.next 
        
        odd.next  = firstEven
        return head