#!/usr/bin/env python3

# https://leetcode.com/problems/container-with-most-water

class Solution:
    def maxArea(self, height: list[int]) -> int:
        area = []
        s, e = 0, len(height) - 1

        while s < e:
            area.append(min(height[s], height[e]) * (e - s))
            if height[s] < height[e]:
                s += 1
            else:
                e -= 1
        return max(area)

n1 = [1,8,6,2,5,4,8,3,7]    # 45
n2 = [1,1]                  # 1
n3 = [2,3,4,5,18,17,6]      # 17

obj = Solution()
print(obj.maxArea(n1))
print(obj.maxArea(n2))
print(obj.maxArea(n3))
