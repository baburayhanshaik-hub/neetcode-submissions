class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        arr = [0 for i in range(n)]
        stack = []
        track = []
        for i,j in list(enumerate(temperatures))[::-1]:
            while stack and stack[-1][0]<=j:
                stack.pop()
            if stack:
                arr[i] = stack[-1][1]-i
            stack.append((j,i))

        return arr