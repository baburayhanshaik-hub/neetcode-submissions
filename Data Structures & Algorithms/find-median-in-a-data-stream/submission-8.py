class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        
        heapq.heappush(self.small,-num)

        if len(self.small)>0 and len(self.large)>0:
            if -self.small[0] > self.large[0]:
                heapq.heappush(self.large, -heapq.heappop(self.small))
            # else:
            #     heapq.heappush(self.small,  heapq.heappop(self.large))
        if len(self.small)>len(self.large)+1:
            val = heapq.heappop(self.small)
            heapq.heappush(self.large, -val)
        if len(self.large)>len(self.small)+1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small,  -val)


    def findMedian(self) -> float:

        if len(self.small)>len(self.large):
            return -self.small[0]
        if len(self.small)<len(self.large):
            return self.large[0]
        return (-self.small[0]+self.large[0])/2