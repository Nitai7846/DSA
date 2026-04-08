#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 22:27:55 2026

@author: nitaishah
"""

# Question: Sort a Linked List of 0s, 1s and 2s (GFG)
#           Given a linked list where each node contains 0, 1, or 2,
#           sort it in ascending order in-place.
#
# Trick: Don't swap values — separate into three chains (zeros, ones, twos)
#        using dummy head nodes, then stitch them together at the end.
#        Watch the stitching order: zero.next must skip the ones dummy head
#        and point to oneHead.next (the actual first 1-node), and fall back
#        to twoHead.next if there are no 1s. Always set two.next = None to
#        avoid a cycle.

class ListNode:
    def __init__(self, x=0, next=None):
        self.data = x
        self.next = next

class Solution:
    def sortList(self, head):
        if head is None or head.next is None:
            return head

        zeroHead = ListNode(-1)
        oneHead = ListNode(-1)
        twoHead = ListNode(-1)

        zero = zeroHead
        one = oneHead
        two = twoHead

        temp = head

        while temp is not None:
            if temp.data == 0:
                zero.next = temp
                zero = temp
            elif temp.data == 1:
                one.next = temp
                one = temp
            elif temp.data == 2:
                two.next = temp
                two = temp
            temp = temp.next

        zero.next = oneHead.next if oneHead.next else twoHead.next
        one.next = twoHead.next
        two.next = None

        return zeroHead.next