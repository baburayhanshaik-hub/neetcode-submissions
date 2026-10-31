class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        dic = defaultdict(int)
        count = 0
        for i in hand:
            dic[i]+=1
        s = set(hand)
        for i in sorted(s):
            if dic[i]!=0:
                for j in range(i+1,i+groupSize):
                    dic[j] = dic[j]-dic[i]
                    if dic[j]<0:
                        return False
                dic[i]=0
        return True