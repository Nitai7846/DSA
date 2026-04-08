#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 22:52:34 2026

@author: nitaishah
"""

# Question: Intersection of Two Linked Lists (LC 160)
#           Given the heads of two singly linked lists, return the node
#           at which they intersect. If they don't intersect, return None.
#
# Trick: Two pointer list-switching trick — run d1 and d2 through their
#        respective lists. When one hits None, redirect it to the HEAD of
#        the OTHER list. They will meet at the intersection node (or both
#        reach None together if no intersection) because both pointers
#        travel the same total distance: len(A) + len(B).
#        No need to compute lengths explicitly.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA is None or headB is None:
            return None

        d1, d2 = headA, headB

        while d1 != d2:
            d1 = d1.next
            d2 = d2.next

            if d1 == d2:
                return d1

            if d1 is None:
                d1 = headB
            if d2 is None:
                d2 = headA

        return d1

# Utility function to insert a node at the end of the linked list
def insertNode(head, val):
    newNode = ListNode(val)
    if head is None:
        return newNode
    temp = head
    while temp.next:
        temp = temp.next
    temp.next = newNode
    return head