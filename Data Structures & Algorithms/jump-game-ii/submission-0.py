class Solution:
    def jump(self, nums: List[int]) -> int:
        i,j,n = 0,0,len(nums)
        count = 0
        while max(i,j)<n-1:
            ans = 0
            for j in range(i+1,min(n,i+nums[i]+1)):
                if j+nums[j]>ans:
                    ans = j+nums[j]
                    i=j
            count+=1
        return count