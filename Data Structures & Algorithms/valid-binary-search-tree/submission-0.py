# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, node):
        def func(l,root,r):
            if root == None:
                return True
            if not l<root.val<r:
                return False
            return func(l,root.left,root.val) and func(root.val,root.right,r)
        return func(float("-inf"),node, float("inf"))