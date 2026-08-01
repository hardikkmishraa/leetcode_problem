class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        max_profit=0
        min_prices=float("inf") #yaha pr -inf nhi lia kiukio obv hume ab chota number dekhna h to ab sif inf lekr chalenege ....jb bada dekhna hota h jaise ki maxi to -inf le kr chalte h 

        for i in range(0,n):
            min_prices=min(min_prices,prices[i])
            max_profit=max(max_profit,prices[i]-min_prices)
        return max_profit