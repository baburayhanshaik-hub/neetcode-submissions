class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        visited = {}
        if not (len(s1+s2) == len(s3)):
            return False
        def func(i,j,k):
            if (i,j,k) in visited:
                return visited[(i,j,k)]
            if i==len(s1) and j==len(s2):
                return True
            if i<len(s1) and j<len(s2) and k<len(s3) and s1[i]==s2[j] and s1[i]==s3[k]:
                visited[(i,j,k)]=func(i+1,j,k+1) or func(i,j+1,k+1)
            elif i<len(s1) and k<len(s3) and s1[i]==s3[k]:
                visited[(i,j,k)]=func(i+1,j,k+1)
            elif j<len(s2) and k<len(s3) and s2[j]==s3[k]:
                visited[(i,j,k)]=func(i,j+1,k+1)
            else:
                visited[(i,j,k)]=False
            return visited[(i,j,k)]
        return func(0,0,0)