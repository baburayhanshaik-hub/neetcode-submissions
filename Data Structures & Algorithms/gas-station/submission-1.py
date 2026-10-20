class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        ans = -1
        prev = 0
        c = 0
        if sum(gas)<sum(cost):
            return -1
        for i,j in zip(gas,cost):
            prev+=i-j
            if prev<0:
                prev = 0
                ans = -1
            elif ans==-1:
                ans = c
            c+=1
        return ans