# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans = None
        def lca(node):
            nonlocal ans
            found = 0
            if node == None or ans!=None:
                return 0
            if node in [p,q]:
                found += 1 + max(lca(node.left), lca(node.right))
            else:
                found += lca(node.left) + lca(node.right)
            if ans==None and found == 2:
                ans = node
                print(ans.val)
            return found
        lca(root)
        
        return ans