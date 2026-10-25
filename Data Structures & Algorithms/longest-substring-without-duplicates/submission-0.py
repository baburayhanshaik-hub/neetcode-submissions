class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r = 0,0
        track = set()
        n = len(s)
        ans = 0
        while r<n:
            while s[r] in track:
                track.remove(s[l])
                l+=1
            track.add(s[r])
            ans = max(ans,r-l+1)
            r+=1
        return ans