class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        d = {}
        res = []
        for i in strs:
            x = ''.join(sorted(i))
            if d.get(x)==None:
                d[x]=[i]
            else:
                d[x].append(i)
        for i,j in d.items():
            res.append(j)
        return res