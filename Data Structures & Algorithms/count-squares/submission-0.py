class CountSquares:

    def __init__(self):
        self.pntscnt = defaultdict(int)
        self.pnts = []

    def add(self, point: List[int]) -> None:
        self.pntscnt[tuple(point)]+=1
        self.pnts.append(point)

    def count(self, point: List[int]) -> int:
        px,py = point
        res = 0
        for x,y in self.pnts:
            if abs(x-px)!=abs(y-py) or px==x or py==y:
                continue
            res+=self.pntscnt[(x,py)]*self.pntscnt[(px,y)]
        return res