#!/usr/bin/env python3

# https://leetcode.com/problems/merge-two-sorted-lists

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1, l2 = list1, list2
        it = ListNode()
        ans = it

        while l1 and l2:
            it.next = ListNode()
            it = it.next
            if l1.val < l2.val:
                it.val = l1.val
                l1 = l1.next
            else:
                it.val = l2.val
                l2 = l2.next

        if l1:
            it.next = l1
        elif l2:
            it.next = l2

        return ans.next
