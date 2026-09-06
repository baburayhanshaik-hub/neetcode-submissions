# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        root.level = 0
        queue = [root]
        ans_map = defaultdict(list)
        while queue:
            node = queue.pop(0)
            ans_map[node.level].append(node.val)
            if node!=None:
                if node.left!=None:
                    node.left.level = node.level+1
                    queue.append(node.left)
                if node.right!=None:
                    node.right.level = node.level+1
                    queue.append(node.right)
        return list(ans_map.values())