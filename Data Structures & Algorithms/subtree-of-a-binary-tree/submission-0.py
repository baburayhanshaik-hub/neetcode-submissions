# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        pointers = []
        def pointer(node, val):
            nonlocal pointers
            if node == None:
                return None
            if node.val == val:
                pointers.append(node)
            pointer(node.left, val)
            pointer(node.right, val)
        pointer(root, subRoot.val)
        def worked(node,subRoot):
            if node==None and subRoot==None:
                return True
            if node==None or subRoot==None:
                return False
            if node.val == subRoot.val:
                if worked(node.left, subRoot.left) and worked(node.right, subRoot.right):
                    return True
            return False

        for i in pointers:
            if worked(i, subRoot):
                return True
        return False
        