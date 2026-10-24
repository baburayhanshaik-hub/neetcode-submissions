class Solution:
    def countBits(self, n: int) -> List[int]:
        arr = [0 for i in range(n+1)]
        x = 0
        for i in range(1,n+1):
            if 2**x==i:
                x+=1
                arr[i] = 1
            else:
                arr[i]= arr[2**(x-1)]+arr[i-2**(x-1)]
        return arr