# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        main_frontier = deque()

        main_frontier.append(root)

        def check_sub(n1, n2):
            s1 = []
            s2 = []
            s1.append(n1)
            s2.append(n2)
            while s1 and s2:
                node1 = s1.pop()
                node2 = s2.pop()
                if not node1 and not node2:
                    continue
                elif not node1 or not node2:
                    return False

                elif node1.val == node2.val:
                    s1.append(node1.left)
                    s1.append(node1.right)
                    s2.append(node2.left)
                    s2.append(node2.right)
                else:
                    return False

            return True

        while main_frontier:
            node = main_frontier.popleft()
            valid = check_sub(node, subRoot)
            if valid:
                return True
            if not node:
                continue
                

            main_frontier.append(node.left)
            main_frontier.append(node.right)

        return False
            
