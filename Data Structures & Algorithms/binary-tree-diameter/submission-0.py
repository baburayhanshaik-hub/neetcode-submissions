# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def func(root):
            nonlocal ans
            if root==None:
                return 0
            left = func(root.left)
            right = func(root.right)
            ans = max(ans,left+right)
            return 1+max(left,right)
        func(root)
        return ans