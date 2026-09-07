# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = float("-inf")
        def func(node):
            nonlocal ans
            if node == None:
                return float("-inf")
            left = func(node.left)
            right = func(node.right)
            
            if node == root:
                ans = max(ans, node.val, left+node.val, right+node.val,left+right+node.val, left, right)
                return max(node.val, left+node.val, right+node.val,left+right+node.val, left, right)
            ans = max(ans, node.val,left+node.val, right+node.val,left+right+node.val)
            return max(node.val,left+node.val, right+node.val)
        val = func(root)
        return ans