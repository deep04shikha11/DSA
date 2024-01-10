# You are given an array prices where prices[i] is the price of a given stock on the ith day, and an integer fee representing a transaction fee.
# Greedy Algo

class Solution:
    def maxProfit(self, prices, fee):
        buy = float('-inf')
        sell = 0

        for price in prices:
            buy = max(buy, sell - price)
            sell = max(sell, buy + price - fee)

        return sell

prices = [1,3,7,5,10,3]
fee = 3
obj = Solution()
print(obj.maxProfit(prices,fee))