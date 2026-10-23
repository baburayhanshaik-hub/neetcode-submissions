class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        s = s.lower()
        r = len(s)-1
        n = len(s)
        while l<r:
            while l<n and not ("a"<=s[l]<="z" or "A"<=s[l]<="Z" or "0"<=s[l]<="9"):
                l+=1
            while r>=0 and not ("a"<=s[r]<="z" or "A"<=s[r]<="Z" or "0"<=s[r]<="9"):
                r-=1
            if l<n and r>=0 and s[l]!=s[r]:
                return False
            l+=1
            r-=1
        return True