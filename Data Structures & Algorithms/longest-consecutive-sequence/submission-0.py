class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        ans,count = 0,0
        for i in nums:
            if i-1 not in nums_set:
                c = i
                count = 0
                while c in nums_set:
                    count+=1
                    c+=1
                ans = max(ans,count)
        return ans