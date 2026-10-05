class Solution:
    def reverse(self, x: int) -> int:
        temp = 0
        if x<0:
            x*=-1
            while x:
                temp*=10
                temp+=x%10
                x=x//10
            return -temp if temp<2**31-1 else 0
        while x:
            temp*=10
            temp+=x%10
            x=x//10
        return temp if temp<2**31-1 else 0