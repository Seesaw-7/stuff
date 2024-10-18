# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # this is still O(N) because it takes O(N) in the worse case
    def countNodes1(self, root: Optional[TreeNode]) -> int:
        depth = 0
        temp = root
        while temp:
            depth += 1
            temp = temp.left

        temp_d = 0
        cnt = 0

        def helper(node, d) -> int:
            nonlocal cnt
            if not node:
                return 1
            d += 1
            if d == depth - 1 and node.left and node.right:
                return 1
            if node.left and not node.right:
                print('yes')
                cnt += 1
                return 1
            if not node.left and not node.right and d != depth:
                cnt += 2
                return 0
            res = 0
            if node.right:
                res = helper(node.right, d)
            if not res:
                return helper(node.left, d)

        helper(root, 0)
        return 2 ** depth - 1 - cnt
            
    def _get_depth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + self._get_depth(root.left)

    # O(logN * logN)
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        l = self._get_depth(root.left)
        r = self._get_depth(root.right)
        if l == r:
            return 2 ** l + self.countNodes(root.right)
        else:
            return 2 ** r + self.countNodes(root.left)