#!/usr/bin/env python3

# https://leetcode.com/problems/longest-consecutive-sequence
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        ans = 0
        nset = set(nums)
        lowest = []

        for i in nset:
            if i-1 not in nset:
                lowest.append(i)

        print("lowest: ", lowest)
        for i in lowest:
            local = 1
            it = i+1
            while it in nset:
                local += 1
                it += 1

            if (ans < local): ans = local

        return ans

obj = Solution()
nums1 = [100,4,200,1,3,2]
nums2 = [7, 5, 3, 8, 2, 100, 2, 1, 4, 56]
nums3 = [0,3,7,2,5,8,4,6,0,1]
nums4 = [9,1,4,7,3,-1,0,5,8,-1,6]
print(obj.longestConsecutive(nums1))    # 4
print(obj.longestConsecutive(nums2))    # 5
print(obj.longestConsecutive(nums3))    # 9
print(obj.longestConsecutive([]))       # 0
print(obj.longestConsecutive(nums4))    # 7
