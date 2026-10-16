class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        collab = [[j,i,(target-j)/i] for i,j in zip(speed,position)]
        collab.sort()
        count = 1
        peak = collab[-1][-1]
        for i in range(len(speed)-2,-1,-1):
            if collab[i][-1]>peak:
                count+=1
                peak = collab[i][-1]
        return count