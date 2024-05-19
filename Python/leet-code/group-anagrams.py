#!/usr/bin/env python3

# https://leetcode.com/problems/group-anagrams/

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

        ans = defaultdict(list)

        for word in strs:
            count = [0] * 26
            for letter in word:
                count[ord(letter) - ord('a')] += 1

            ans[tuple(count)].append(word)

        return list(ans.values())

obj = Solution()

print(obj.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
