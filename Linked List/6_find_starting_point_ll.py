#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 23:20:24 2026

@author: nitaishah
"""


# Question: Find the Starting Point of a Loop in a Linked List (LC 142)
#           Given a linked list that may contain a cycle, return the node
#           where the cycle begins. If there is no cycle, return None.
#
# Trick: Floyd's Cycle Detection — two phases.
#        Phase 1: Move slow by 1, fast by 2. If they meet, a cycle exists.
#        Phase 2: Reset slow to head, keep fast at meeting point.
#                 Move BOTH by 1 step at a time — they will meet exactly
#                 at the cycle's entry node.
#        The math: the distance from head to cycle start equals the
#        distance from the meeting point to cycle start (going forward),
#        which is why resetting slow to head works.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def findStartingPoint(self, head):
        slow = head
        fast = head

        # Phase 1: Detect the loop
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                # Phase 2: Find entry point
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow

        return None