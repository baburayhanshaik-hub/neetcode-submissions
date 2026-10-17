class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        i = 0
        while i<len(nums):
            ans = 0
            for x in range(i+1,i+nums[i]+1):
                if x>=n:
                    return True
                if i+nums[x]>=ans:
                    ans = i+nums[x]
                    i = x
            if i==n-1:
                return True
            if nums[i]==0:
                return False
        return True