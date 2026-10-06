class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l = [0 for _ in range(n)]
        r = [0 for _ in range(n)]
        for i in range(n):
            l[i] = max(height[i],l[i-1])
        for j in range(n-1,-1,-1):
            print(r[j])
            r[j] = max(height[j],r[(j+1)%n])
        ans = 0
        for i in range(n):
            ans+=min(l[i],r[i])-height[i]
        return ans