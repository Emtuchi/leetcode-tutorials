from typing import List
class Solution:
    def Profit(self, prices: List[int]) -> int:
        l, r = 0, 1 #left=buy, right=sell, 0,1 rep 1st and 2nd index
        maxP = 0
        while r < len(prices):
            if prices[l] > prices[r]:
                l = r
            else:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            r += 1
        print(maxP)