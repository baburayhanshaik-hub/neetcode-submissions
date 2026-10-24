class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        x = 31
        while n:
            temp = 1&n
            ans+=temp<<x
            n=n>>1
            x-=1
        print(ans)
        return ans