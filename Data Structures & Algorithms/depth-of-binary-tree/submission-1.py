# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # count = 0
        d = deque()
        d.append(root)
        depth = 0
        if not root:
            return 0

        while d:
            level = len(d)
            for _ in range(level):
                node = d.popleft()
                if node:
                    d.append(node.left)
                    d.append(node.right)
            depth += 1
        return depth -1

        
        # level = 1
        # depth = 0
        # if not root:
        #     return 0

        # while d:
        #     node = d.popleft()
        #     count += 1
        #     if node:
        #         d.append(node.left)
        #         d.append(node.right)
        #     if count == level:
        #         if level == 1:
        #             level = 2
        #         else:
        #             level = level **2
        #         depth += 1
        # return depth
        



        