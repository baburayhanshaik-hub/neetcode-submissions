class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        x = [-i for i in Counter(tasks).values()]
        heapq.heapify(x)
        d = deque()
        time = 0
        while x or d:
            time+=1
            if x:
                val = heapq.heappop(x)
                if val+1!=0:
                    d.append((val+1,time+n))
            if len(d)>0 and d[0][1]==time:
                heapq.heappush(x,d.popleft()[0])
        return time