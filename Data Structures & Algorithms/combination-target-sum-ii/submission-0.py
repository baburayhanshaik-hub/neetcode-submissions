class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        trace = {}
        candidates.sort()
        if sum(candidates)<target:
            return ans
        def func(ind,target,res):
            nonlocal ans,trace
            n = len(candidates)
            if ind>n:
                return 
            if target == 0:
                return 0
            elif target < 0:
                return None
            for i in range(ind,n):
                if i>ind and candidates[i]==candidates[i-1]:
                    continue
                if candidates[i]>target:
                    break
                if func(i+1,target-candidates[i], res+[candidates[i]])==0:
                    ans.append(res+[candidates[i]])
        func(0,target,[])
        print(sum([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]))
        return ans