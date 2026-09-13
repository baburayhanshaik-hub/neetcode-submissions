"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node==None:
            return None
        visited = {}
        def func(node):
            if visited.get(node):
                return visited.get(node)
            
            clone = Node(node.val)
            visited[node] = clone

            for i in node.neighbors:
                clone.neighbors.append(func(i))
            return clone

        return func(node)