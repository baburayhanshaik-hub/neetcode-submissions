class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        visited = {}
        def func(i,state):
            if i>=len(prices):
                return 0
            if visited.get((i,state)):
                return visited[(i,state)]
            cool = func(i+1, state)
            if state==True:
                buy = -prices[i]+func(i+1,not state)
                visited[(i,state)] = max(buy,cool)
            else:
                sell = prices[i]+func(i+2, not state)
                visited[(i,state)] = max(sell,cool)
            return visited[(i,state)]
        return func(0,True)