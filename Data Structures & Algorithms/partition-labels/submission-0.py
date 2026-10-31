class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d = {}
        for i,j in enumerate(s):
            d[j] = i
        
        l,r,n = 0,0,len(s)

        dist = 0
        res = []
        while r<n:
            dist = max(d[s[r]],dist)
            if r==dist:
                res.append(r-l+1)
                l=r+1
            r+=1
        return res