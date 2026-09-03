# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        ans = 1
        def func(root):
            nonlocal ans
            if root == None:
                return 0
            left  = func(root.left)
            right = func(root.right)
            print(right, left)
            if abs(right-left)>1:
                ans*=0
            return 1+max(left,right)
        func(root)
        return False if ans==0 else True