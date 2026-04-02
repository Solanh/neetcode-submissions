# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        frontier = deque()
        frontier.append(root)

        order = []
        
        
        while frontier:
            level = frontier
            frontier = deque()
            l = []
            while level:
                node = level.popleft()
                if node:
                    l.append(node.val)
                    frontier.append(node.left)
                    frontier.append(node.right)
            order.append(l)

        return order[:len(order)-1]





            


        