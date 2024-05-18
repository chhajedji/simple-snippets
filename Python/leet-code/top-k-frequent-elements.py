#!/usr/bin/env python3

# https://leetcode.com/problems/top-k-frequent-elements/

from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counts = defaultdict(int)

        for i in nums:
            counts[i] += 1

        rev_counts = defaultdict(list)
        for (a, b) in counts.items():
            rev_counts[b].append(a)

        rev_counts = sorted(rev_counts.items(), reverse = True)
        ans = []
        j, i = 0, 0

        while i < k:
            ans += rev_counts[j][1]
            i += len(rev_counts[j][1])
            j += 1

        return ans

obj = Solution()
obj2 = Solution()

print(obj.topKFrequent([1,1,1,2,2,3], 2))
print(obj2.topKFrequent([4, 5, 1, 3, 4, 5, 1, 5, 3, 4, 1], 3))
print(obj2.topKFrequent([1], 1))
