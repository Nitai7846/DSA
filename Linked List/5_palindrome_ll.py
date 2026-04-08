#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 23:10:18 2026

@author: nitaishah
"""

# Question: Palindrome Linked List (LC 234)
#           Given the head of a singly linked list, return True if it is a
#           palindrome, False otherwise.
#
# Trick: Two phases —
#        1) Find the middle using slow/fast pointers (slow ends at mid).
#        2) Reverse the second half (slow.next onward) and compare
#           node-by-node with the first half.
#        Restore the second half by reversing it again before returning.
#        The slow/fast loop condition is fast.next and fast.next.next
#        (not fast and fast.next) so that slow lands at the LEFT middle
#        for even-length lists, giving the correct split point.

class ListNode:
    def __init__(self, data1=0, next1=None):
        self.val = data1
        self.next = next1

class Solution:

    def reverseLinkedList(self, head):
        prev = None
        curr = head

        while curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        return prev

    def isPalindrome(self, head):
        if head is None or head.next is None:
            return True

        slow = head
        fast = head

        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next

        newHead = self.reverseLinkedList(slow.next)

        first = head
        second = newHead

        while second is not None:
            if first.val != second.val:
                self.reverseLinkedList(newHead)
                return False
            first = first.next
            second = second.next

        self.reverseLinkedList(newHead)
        return True