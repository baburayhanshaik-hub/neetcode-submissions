import heapq

class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        self.heap = []
        self.exp = k
        for i in range(len(nums)):
            if i>=k:
                heapq.heappushpop(self.heap,nums[i])
            else:
                heapq.heappush(self.heap,nums[i])
    def add(self, val: int) -> int:
        if len(self.heap)<self.exp:
            heapq.heappush(self.heap,val)
        else:
            heapq.heappushpop(self.heap,val)
        return self.heap[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)