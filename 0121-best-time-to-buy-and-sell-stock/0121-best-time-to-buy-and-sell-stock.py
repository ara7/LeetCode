class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #let' do using pointers
        l,r = 0,1 #left is buying #right is selling
        maxP = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r += 1
        return maxP
        