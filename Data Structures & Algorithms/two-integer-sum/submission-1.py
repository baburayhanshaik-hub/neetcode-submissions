class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic ={}
        for i,j in enumerate(nums):
            if j not in dic:
                dic[j]=i
        
        for i in range(len(nums)-1,-1,-1):
            if target-nums[i] in dic:
                return [dic[target-nums[i]],i]