#!/usr/bin/env python3

# https://leetcode.com/problems/copy-list-with-random-pointer/

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return None

        l1 = head
        link = {}

        while l1:
            node = Node(l1.val)
            link[l1] = node
            l1 = l1.next

#        print("link.items(): ", link.items()[0])
        l2 = list(link.items())[0][1]
        l1 = head

        while l1:
            if l1.random: l2.random = link[l1.random]
            else: l2.random = None
            if l1.next:
                l2.next = link[l1.next]
            else:
                l2.next = None
            l1 = l1.next
            l2 = l2.next


        return list(link.items())[0][1]
