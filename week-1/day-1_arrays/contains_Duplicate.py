from typing import List

class Solution:
    def unique(self, nums: List[int]):
        dic = {}
        for index, value in enumerate(nums):
            if value in dic:
                return True
            dic[value] = index
        
        return False