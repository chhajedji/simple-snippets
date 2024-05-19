#!/usr/bin/env python3

# https://leetcode.com/problems/valid-palindrome

class Solution:
    def isPalindrome(self, s: str) -> bool:

        st = ''
        for c in s.lower():
            if c.isalnum(): st += c

        return st == st[::-1]

obj = Solution()
s1 = "A man, a plan, a canal: Panama"   # True
s2 = "race a car"                       # False
s3 = " "                                # True
print(obj.isPalindrome(s1))
print(obj.isPalindrome(s2))
print(obj.isPalindrome(s3))
