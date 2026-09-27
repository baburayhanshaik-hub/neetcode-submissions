class Solution:
    def rob(self, nums: List[int]) -> int:
        visited = {}
        def func(i):
            if i>=len(nums):
                return 0
            if i in visited:
                return visited[i]
            ans = max(nums[i]+func(i+2), func(i+1))
            visited[i] = ans
            return ans
        return func(0)