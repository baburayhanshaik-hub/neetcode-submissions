class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0,len(nums)-1
        def find_min():
            l,r = 0,len(nums)-1
            while l<=r:
                mid = l+(r-l)//2
                if nums[l]<=nums[r]:
                    return l
                if nums[mid]<nums[mid-1]:
                    return mid
                if nums[mid]<nums[l]:
                    r = mid-1
                else:
                    l = mid+1
        mini = find_min()
        if nums[r]>=target>=nums[mini]:
            l = mini
        else:
            r = mini
        while l<=r:
            mid = l+(r-l)//2
            print(l,r,mid)
            if nums[mid]==target:
                return mid
            if nums[mid]<target:
                l=mid+1
            else:
                r=mid-1
        return -1