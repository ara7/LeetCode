class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prof = 0
        first_ele = prices[0]
        for price in prices[1:]:
            #update first_ele if current_price is lower than current buying price
            if first_ele > price:
                first_ele = price

            elif price - first_ele > prof:
                prof = price - first_ele 
        return prof
        '''prof = []
        for i in range(len(prices)):
            for j in range(1, len(prices)):
                if prices[i] < prices[j]:
                    prof.append(prices[j] - prices[i])
        return max(prof)''' #This solution fails some cases and uses two loops
         
        