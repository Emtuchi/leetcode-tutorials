from typing import List

class Solution:
    def maxprod(self, nums: List[int]):
        left, right = 0, 1
        result = 0

        while right < len(nums):
            prod = nums[left] * nums[right]
            result = max(prod, result)

            right += 1
            left += 1

        print(result)