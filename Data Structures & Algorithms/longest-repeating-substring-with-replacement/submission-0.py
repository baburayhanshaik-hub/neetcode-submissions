class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l,r = 0,0
        n = len(s)
        a_dic = [0 for i in range(26)]
        ans = 0
        while r<n:
            a_dic[ord(s[r])-ord("A")]+=1
            maxi = max(a_dic)
            while l<=r and r-l+1-maxi>k:
                a_dic[ord(s[l])-ord("A")]-=1
                l+=1
            ans = max(ans,r-l+1)
            r+=1
        return ans