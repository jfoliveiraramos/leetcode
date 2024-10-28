# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional, List, Dict, Tuple 
from collections import defaultdict

class Solution:


    def getHeights(self, node: Optional[TreeNode], heightDepths: Dict[int, Tuple[int,int]], max_heights: Dict[int, Tuple[int, int]], depth: int) -> int:
        
        if not node:
            return -1

        left = self.getHeights(node.left, heightDepths, max_heights, depth + 1)
        right = self.getHeights(node.right, heightDepths, max_heights, depth + 1)
        height = max(left, right) + 1
        heightDepths[node.val] = (height, depth)

        height1, height2 = max_heights[depth]
        if height > height1:
            max_heights[depth] = (height, height1)
        elif height > height2:
            max_heights[depth] = (height1, height)

        return height
        
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:

        heightDepths = {}
        max_heights : Dict[int, Tuple[int, int]] = defaultdict(lambda: (-1, -1))

        self.getHeights(root, heightDepths, max_heights, 0)

        ans = [] 

        total_height = heightDepths[root.val][0] if root else 0

        for query in queries:

            height, depth = heightDepths[query]
            height1, height2 = max_heights[depth]

            if height == height1:
                ans.append(total_height - height1 + height2)
            else:
                ans.append(total_height)

        return ans
        
