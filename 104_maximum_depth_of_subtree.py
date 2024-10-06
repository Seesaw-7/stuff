# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    # divide and conquer recursion (recursive DFS)
    def _depth_helper(self, node, max_lvl: int) -> int:
        if not node:
            return max_lvl
        left_max = self._depth_helper(node.left, max_lvl + 1)
        right_max = self._depth_helper(node.right, max_lvl + 1)
        return max(left_max, right_max)

    def maxDepth1(self, root: Optional[TreeNode]) -> int:
        max_lvl = 0
        return self._depth_helper(root, max_lvl)

    # DFS (iterative)
    def maxDepth2(self, root: Optional[TreeNode]) -> int:
        max_level = 0
        stack = [(root, 0)]

        while stack:
            curr = stack.pop()
            if not curr[0]:
                max_level = max(max_level, curr[1])
            else:
                stack.append((curr[0].left, curr[1]+1))
                stack.append((curr[0].right, curr[1]+1))
        return max_level

    # BFS
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_level = 0
        nodes = deque([(root, 0)])

        while nodes:
            curr = nodes.popleft()
            if not curr[0]:
                max_level = max(max_level, curr[1])
            else:
                nodes.append((curr[0].left, curr[1]+1))
                nodes.append((curr[0].right, curr[1]+1))

        return max_level

    