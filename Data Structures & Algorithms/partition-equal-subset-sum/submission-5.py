class Solution:
    def canPartition(self, nums):
        def func(x,half):
            if half == 0:
                return True
            if half<0:
                return False
            for i in range(x,len(nums)):
                if func(i+1,half-nums[i]):
                    return True
            return False
        half = sum(nums)//2
        if sum(nums)%2:
            return False
        return func(0,half)