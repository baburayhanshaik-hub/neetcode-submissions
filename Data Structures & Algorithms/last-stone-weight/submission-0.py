import heapq
class Solution:
    def lastStoneWeight(self, st: list[int]) -> int:
        if len(st)<2:
            return 0 if st==[] else st[0]
        res = []
        stones = []
        for i in st:
            heapq.heappush(stones,-i)
        print(stones)
        while True:
            if len(res)==2:
                print(res,abs(-res[0]-(-res[1])))
                diff = abs(-res[0]-(-res[1]))
                heapq.heappush(stones,-diff)
                res = []
                if len(stones)==1:
                    break
            res.append(heapq.heappop(stones))
        return -stones[0]