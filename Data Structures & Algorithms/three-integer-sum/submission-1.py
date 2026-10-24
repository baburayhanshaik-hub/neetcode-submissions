class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # nums.sort()
        n = len(nums)
        ans = []
        check = set()
        check_trip = set()
        for i in range(n):
            for j in range(i+1,n):
                x = -(nums[i]+nums[j]) 
                if x in check and tuple(sorted([nums[i],nums[j],x])) not in check_trip:
                    check_trip.add(tuple(sorted([nums[i],nums[j],x])))
                    ans.append([nums[i],nums[j],x])
            check.add(nums[i])
        return ans