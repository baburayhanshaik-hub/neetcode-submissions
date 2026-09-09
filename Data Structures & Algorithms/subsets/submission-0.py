class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        visited = {}
        n = len(nums)
        def func(track,t):
            nonlocal ans, visited, n
            if t>n:
                return
            ans.append(track)
            for i in range(t,n):
                func(track+[nums[i]],i+1)
        func([],0)
        print(ans)
        return ans