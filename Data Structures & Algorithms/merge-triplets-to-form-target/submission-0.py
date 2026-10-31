class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        stack = []
        n = len(triplets)
        track = [1 for i in range(n)]
        j = 0
        def func(k):
            res = []
            # print(triplets)
            for i,j in enumerate(triplets):
                if track[i]==1:
                    if j[k]>target[k]:
                        track[i]=0
        for i in range(0,3):
            res = func(i)
            # triplets = res
        res = [float("-inf") for i in range(3)]
        for i in range(n):
            if track[i]==1:
                for j in range(3):
                    res[j] = max(res[j],triplets[i][j])
        return res == target