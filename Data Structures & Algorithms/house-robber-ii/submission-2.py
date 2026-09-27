class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        def func(i,nums):
            if i>=len(nums):
                return 0
            if i in visited:
                return visited[i]
            ans = max(nums[i]+func(i+2,nums), func(i+1,nums))
            visited[i] = ans
            return ans
        visited = {}
        ans1 = func(0,nums[0:len(nums)-1])
        visited = {}
        ans2 = func(0, nums[1:])
        return max(ans1, ans2)