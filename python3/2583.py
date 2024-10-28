from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:

        sums = []

        if root is None:
            return -1
        
        queue = deque()

        queue.append(root)

        while len(queue):

            n = len(queue)
            sum = 0

            for _ in range(n):

                node = queue.popleft()

                sum += node.val

                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)

            sums.append(sum)

        if len(sums) < k:
            return -1

        sums.sort()

        return sums[len(sums) - k]

     
