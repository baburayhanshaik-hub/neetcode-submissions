class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for i in nums:
            if i in dic:
                dic[i]+=1
            else:
                dic[i] = 1
        track = []
        for i,j in dic.items():
            heapq.heappush(track,(j,i))
            if len(track)>k:
                heapq.heappop(track)
        return [j for i,j in track]