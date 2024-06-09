from typing import List

class Solution:
    def ThreeSUM(self, nums: List[int]):
        output = []
        l,r_a,r_b, = 0,1,2
        hash_tup = {}
        i = 0

        while l < len(nums):
            while r_b < len(nums):
                temp = []
                if (nums[l] + nums[r_a] + nums[r_b] == 0):
                    temp = [nums[l], nums[r_a], nums[r_b]]
                    if (tuple(sorted(temp)) not in hash_tup):
                        output.append(temp)
                    hash_tup[tuple(sorted(temp))] = i
                    i += 1
                r_b += 1
                r_a += 1
            l += 1
            r_a = l + 1
            r_b = l + 2
        print(output)
