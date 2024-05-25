#!/usr/bin/env python3

# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode()
        prev = ans
        carry = 0
        i = 0

        while l1 and l2:
            prev.next = ListNode((l1.val + l2.val + carry) % 10)
            carry = (l1.val + l2.val + carry) // 10
            l1, l2 = l1.next, l2.next
            prev = prev.next
            print(f"i: {i}\tprev.val: {prev.val}")
            i += 1

        while l1:
            prev.next = ListNode((l1.val + carry) % 10)
            carry = (l1.val + carry) // 10
            prev = prev.next
            l1 = l1.next
            print(f"i: {i}\tprev.val: {prev.val}")
            i += 1
        
        while l2:
            prev.next = ListNode((l2.val + carry) % 10)
            carry = (l2.val + carry) // 10
            prev = prev.next
            l2 = l2.next
            print(f"i: {i}\tprev.val: {prev.val}")
            i += 1

        if carry:
            prev.next = ListNode(carry)
            prev = prev.next
            print(f"i: {i}\tprev.val: {prev.val}")
            i += 1

        return ans.next

