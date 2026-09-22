class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        visited = {}
        nums = [1]+nums+[1]
        def func(left, right):
            if left+1>=right:
                return 0
            ans = 0
            if (left,right) in visited:
                return visited[(left,right)]
            for i in range(left+1,right):
                x = func(i,right)
                y = func(left,i)
                ans = max(ans,
                    y+nums[left]*nums[i]*nums[right]+x
                )
            visited[(left,right)] = ans
            return ans
        res = func(0,len(nums)-1)
        return res