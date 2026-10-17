class Solution:
    def insert(self, iv: List[List[int]], new: List[int]) -> List[List[int]]:
        n = len(iv)
        res = []
        for i in range(n):
            if new[1]<iv[i][0]:
                res.append(new)
                return res+iv[i:]
            elif new[0]>iv[i][1]:
                res.append(iv[i])
            else:
                new = [min(iv[i][0],new[0]),max(iv[i][1],new[1])]
        res.append(new)
        return res