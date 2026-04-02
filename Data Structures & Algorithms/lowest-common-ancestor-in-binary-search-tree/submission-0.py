# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        frontier = deque()
        frontier.append(root)

        def check_sub(node):
            frontier = deque()
            frontier.append(node)
            
            while frontier:
                node = frontier.popleft()
                if node:
                    if node.val == p.val or node.val == q.val:
                        return True
                    frontier.append(node.left)
                    frontier.append(node.right)
            return False


        while frontier:
            node = frontier.popleft()

            if node:
                b1 = check_sub(node.left)
                b2 = check_sub(node.right)
                print(b1, b2)

                if b1 and b2:
                    return node
                elif node.val == q.val or node.val == p.val:
                    return node
                elif b1 and not b2:
                    frontier.append(node.left)
                else:
                    frontier.append(node.right)




