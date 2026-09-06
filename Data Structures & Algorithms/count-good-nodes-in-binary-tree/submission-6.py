# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = 0
        def func(node, track):
            if node == None:
                return 0
            nonlocal ans
            if node.val >= track:
                ans+=1
            func(node.left,track if track>node.val else node.val)
            func(node.right,track if track>node.val else node.val)
        func(root,root.val)
        return ans