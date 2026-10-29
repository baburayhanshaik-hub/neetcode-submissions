class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        def check():
            pass
        maxi = float("-inf")
        for i in range(k):
            if nums[i]>=maxi:
                maxi = nums[i]
                m_ind = i
        res = [maxi]
        n = len(nums)
        l = 0
        for r in range(k,n):
            l+=1
            if m_ind<l:
                maxi = float("-inf")
                for k in range(l,r+1):
                    if nums[k]>=maxi:
                        maxi = nums[k]
                        m_ind = k
            if nums[r]>=maxi:
                maxi = nums[r]
                m_ind = r
            res.append(maxi)
        return res