# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(head):
            prev = None
            mid = temp = head
            n = 0
            while mid:
                n+=1
                mid = temp.next
                temp.next = prev
                prev = temp
                temp = mid
            return prev,n
        res,n = reverse(head)
        rem = n%k
        prev = None
        if rem:
            prev = end = res
            for i in range(rem-1):
                end = end.next
            res = end.next
            end.next = None
            prev,_ = reverse(prev)
        for i in range(rem,n,k):
            first = end = res
            for j in range(i,i+k-1):
                end = end.next
            res = end.next
            end.next = prev
            prev = first
        return prev