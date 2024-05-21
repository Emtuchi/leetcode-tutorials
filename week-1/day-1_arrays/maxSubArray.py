from typing import List

class Solution:
    def maxSub(self, nums: List[int]) -> int:
        maxsub = nums[0]
        cursor = 0

        for i in nums:
            if cursor < 0:
                cursor = 0
            cursor += i
            maxsub = max(maxsub, cursor)
        
        print(maxsub)