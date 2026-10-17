class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l,r = 0,len(nums)-1
        while l<r:
            if nums[l]+nums[r]>target:
                r-=1
            else:
                if nums[l]+nums[r]==target:
                    return [l+1,r+1]
                l+=1
        return [l+1,r+1]