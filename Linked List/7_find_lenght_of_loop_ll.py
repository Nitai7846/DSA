#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 23:51:51 2026

@author: nitaishah
"""
# Question: Find the Length of a Loop in a Linked List (GFG)
#           Given a linked list that may contain a cycle, return the number
#           of nodes in the cycle. If there is no cycle, return 0.
#
# Trick: Floyd's detection to find the meeting point (phase 1), then count
#        the loop length by holding slow fixed and walking fast around the
#        loop until it laps back to slow — counting each step taken.
#        Initialise cnt = 1 and advance fast once BEFORE the while loop
#        so you don't immediately exit (slow == fast is already true at start).

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def findLength(self, slow, fast):
        cnt = 1
        fast = fast.next

        while slow != fast:
            cnt += 1
            fast = fast.next

        return cnt

    def findLengthOfLoop(self, head):
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return self.findLength(slow, fast)

        return 0