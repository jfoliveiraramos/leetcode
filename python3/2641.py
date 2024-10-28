from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root:
            return None

        q = deque([root])
        sums = []

        while q:
            level_sum = 0

            for _ in range(len(q)):
                node = q.popleft()
                if node:

                    level_sum += node.val

                    if node.left:
                        q.append(node.left)

                    if node.right:
                        q.append(node.right)

            sums.append(level_sum)

        root.val = 0
        q.append(root)
        k = 1

        while k < len(sums):

            next_sum = sums[k]

            for _ in range(len(q)):

                node = q.popleft()
                if node:
                    left_val = node.left.val if node.left else 0
                    right_val = node.right.val if node.right else 0

                    new_val = next_sum - left_val - right_val

                    if node.left:
                        node.left.val = new_val
                        q.append(node.left)

                    if node.right:
                        node.right.val = new_val
                        q.append(node.right)

            k += 1

        return root
