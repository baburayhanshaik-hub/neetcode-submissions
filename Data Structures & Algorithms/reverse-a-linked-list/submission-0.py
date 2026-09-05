# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        left = None
        mid = head
        right = head
        while right != None:
            right = right.next
            mid.next = left
            left = mid
            mid = right
        return left
