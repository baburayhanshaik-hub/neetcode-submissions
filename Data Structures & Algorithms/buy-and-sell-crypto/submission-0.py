class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        mini = float("inf")
        for i in prices:
            mini = min(i,mini)
            ans = max(ans, i-mini)
        return ans