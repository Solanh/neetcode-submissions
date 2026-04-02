# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        frontier = []
        frontier.append((root, float("-inf"), float("inf")))

        while frontier:
            node, min_v, max_v = frontier.pop()

            if node:
                if min_v < node.val < max_v:
                    frontier.append((node.left, min_v, node.val))
                    frontier.append((node.right, node.val, max_v))
                
                else:
                    return False

        return True





