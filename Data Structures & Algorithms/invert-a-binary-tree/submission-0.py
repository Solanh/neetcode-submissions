# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if root == []:
            return root

        d = deque()
        d.append(root)

        while d:
            node = d.pop()
            if node:
                node.right, node.left = node.left, node.right
                d.appendleft(node.right)
                d.append(node.left)
            # elif node.right:
            #     node.left = node.right
            #     node.right = None
            # else:
            #     node.right = node.left
            #     node.left = None
            

        return root






        