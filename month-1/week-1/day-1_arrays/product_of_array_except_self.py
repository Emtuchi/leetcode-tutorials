from typing import List

class Solution:
    def product(self, nums: List[int]) -> List[int]:
        # initialise the arrays to use
        left = [0] * (len(nums))
        right = [0] * (len(nums))
        product = [0] * (len(nums))

        left[0] = 1 # make first element from the left 1
        right[len(nums) - 1] = 1 # do the above the  right

        for i in range(1, len(nums)):
            left[i] = nums[i - 1] * left[i - 1]

        for i in range(len(nums) -2, -1, -1):
            right[i] = nums[i + 1] * right[i + 1]
        
        for i in range(len(nums)):
            product[i] = left[i] * right[i]

        print(product)