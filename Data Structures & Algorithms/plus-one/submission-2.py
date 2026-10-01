class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        rem = 0
        quo = 1
        for i in range(len(digits)-1,-1,-1):
            rem = (digits[i]+quo)%10
            quo = (digits[i]+quo)//10
            digits[i] = rem
        if quo:
            digits = [1]+digits
        return digits