#!/usr/bin/env python3

# https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        ans = [1 for i in range(len(nums))]

        for i in range(1, len(nums)):
            ans[i] = ans[i-1] * nums[i-1]

        post_val = 1

        for i in range(len(nums)-2, -1, -1):
            post_val *= nums[i+1]
            ans[i] = ans[i] * post_val

        return ans

obj = Solution()

print(obj.productExceptSelf([-3, -2, 2, 3, 1]))
