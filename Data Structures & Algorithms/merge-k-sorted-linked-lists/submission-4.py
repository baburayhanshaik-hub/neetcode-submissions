# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge2lists(l1,l2):
            temp = res = ListNode()
        def merge2lists(l1, l2):
            temp = res = ListNode()

            while l1 or l2:
                if not l2 or (l1 and l1.val <= l2.val):
                    res.next = l1
                    l1 = l1.next
                else:
                    res.next = l2
                    l2 = l2.next

                res = res.next

            return temp.next

        def reslist(l):
            if not l:
                return [None]
            
            while len(l)>1:
                mergedlists = []
                for i in range(0,len(l),2):
                    l1 = l[i]
                    l2 = l[i+1] if i+1<len(l) else None
                    mergedlists.append(merge2lists(l1,l2))
                l = mergedlists

            return l
        return reslist(lists)[0]
