import heapq

class MinStack:
    def __init__(self):
        self.dabba = []

    def push(self, val: int) -> None:
        self.dabba.append(val)

    def pop(self) -> None:
        self.dabba.pop()

    def top(self) -> int:
        return self.dabba[-1]

    def getMin(self) -> int:
        return min(self.dabba)