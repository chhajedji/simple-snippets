#!/usr/bin/env python3

# https://leetcode.com/problems/reverse-linked-list/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

n1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
n2 = ListNode(1)


obj = Solution()
print(obj.reverseList(n1))
print(obj.reverseList(n2))
