# Approach using minimum so far to get max profit
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minSoFar = prices[0]
        maxProfit = 0
        for price in prices:
            minSoFar = min(minSoFar, price)
            maxProfit = max(maxProfit, price - minSoFar)
        
        return maxProfit

# Time: O(n)
# Space: O(1)

# # Two pointer approach
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         l = 0
#         r = 1
#         maxProfit = 0
#         while r < len(prices):
#             buy = prices[l]
#             sell = prices[r]
#             maxProfit = max(maxProfit, sell - buy)
#             if buy < sell:
#                 r += 1
#             else:
#                 l = r
#                 r += 1

#         return maxProfit

# # Time: O(n)
# # Space: O(1)