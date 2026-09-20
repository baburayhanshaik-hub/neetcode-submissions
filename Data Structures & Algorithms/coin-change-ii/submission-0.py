class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        visited = {}
        def func(i,amount):
            if (i,amount) in visited:
                return visited[(i,amount)]
            if amount==0:
                return 1
            if amount<0 or i>=len(coins):
                return 0
            visited[(i,amount)] = func(i,amount-coins[i]) + func(i+1, amount)
            return visited[(i,amount)]
        return func(0,amount)