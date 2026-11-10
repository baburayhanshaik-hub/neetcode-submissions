class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        visited = set()
        for i in nums:
            if i in visited:
                return i
            visited.add(i)