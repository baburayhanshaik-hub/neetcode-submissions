class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0,len(nums)-1
        while l<=r:
            mid = l+(r-l)//2
            if nums[l]<=nums[r]:
                return nums[l]
            if nums[mid]<nums[mid-1]:
                return nums[mid]
            if nums[mid]<nums[l]:
                r = mid-1
            else:
                l = mid+1