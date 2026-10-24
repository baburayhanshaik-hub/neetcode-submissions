class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1 for i in range(n)]

        temp = nums[0]
        for i in range(1,n):
            ans[i]=ans[i-1]*nums[i-1]
        temp = nums[-1]
        for i in range(n-2,-1,-1):
            ans[i]=ans[i]*temp
            temp*=nums[i]
        
        return ans