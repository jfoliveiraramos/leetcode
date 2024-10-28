
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False

        stack1 : List[Optional[TreeNode]] = [root1]
        stack2 : List[Optional[TreeNode]] = [root2]

        while stack1 and stack2:
            node1 = stack1.pop()
            node2 = stack2.pop()

            if not node1 and not node2:
                continue
            if not node1 or not node2:
                return False
            if node1.val != node2.val:
                return False

            if (self.areNodesEqual(node1.left, node2.left) and 
                self.areNodesEqual(node1.right, node2.right)):
                stack1.append(node1.left)
                stack2.append(node2.left)
                stack1.append(node1.right)
                stack2.append(node2.right)

            elif (self.areNodesEqual(node1.left, node2.right) and 
                  self.areNodesEqual(node1.right, node2.left)):
                stack1.append(node1.left)
                stack2.append(node2.right)
                stack1.append(node1.right)
                stack2.append(node2.left)

            else:
                return False

        return len(stack1) == len(stack2) == 0

    def areNodesEqual(self, node1: Optional[TreeNode], node2: Optional[TreeNode]) -> bool:
        if not node1 and not node2:
            return True
        if not node1 or not node2:
            return False
        return node1.val == node2.val
