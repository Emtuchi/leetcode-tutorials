from typing import List

class solution:
    def twosum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}

        for index, value in enumerate(nums):
            diff = target - value
            if diff in prevMap:
                return [prevMap[diff], index]
            prevMap[value] = index
        return