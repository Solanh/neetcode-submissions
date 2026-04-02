class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r  = 0 , len(prices)

        

        buy = float("inf")
        best = 0

        for p in prices:
            
            buy = min(buy, p)
            
            best = max(best, p - buy)
        return best


