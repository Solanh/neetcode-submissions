# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import heapq
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        frontier = []
        vals = []
        frontier.append(root)

        while frontier:
            node = frontier.pop()

            if node:
                heapq.heappush(vals, node.val)
                frontier.append(node.left)
                frontier.append(node.right)

        for i in range(k):
            if i == k -1:
                return heapq.heappop(vals)
            heapq.heappop(vals)
