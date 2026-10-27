class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_dic = {}
        s2_dic = {}
        l = 0
        for i in s1:
            s1_dic[i]=1+s1_dic.get(i,0)
        for i in s2:
            s2_dic[i]=1+s2_dic.get(i,0)
        n,m = len(s1),len(s2)
        for r in range(m):
            s1_dic[s2[r]]=s1_dic.get(s2[r],0)-1

            while l<=r and s1_dic[s2[r]]<0:
                s1_dic[s2[l]]+=1
                l+=1
            if r-l+1==n:
                return True
        return False