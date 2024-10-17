# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum1(self, root: Optional[TreeNode]) -> int:
        def helper(node: Optional[TreeNode]) -> (int, int):
            if not node:
                return 0, 0
            if not node.left and not node.right:
                return node.val, node.val
            elif not node.right:
                a = helper(node.left)
                max_con = max(a[0]+node.val, node.val)
                max_discon = max(a[1], a[0])
                return max_con, max_discon
            elif not node.left:
                b = helper(node.right)
                max_con = max(b[0]+node.val, node.val)
                max_discon = max(b[1], b[0])
                return max_con, max_discon
            a = helper(node.left)
            b = helper(node.right)
            max_con = max(max(a[0], b[0]) + node.val, node.val)
            max_discon = max(a[1], b[1], a[0]+b[0]+node.val, a[0], b[0])
            return max_con, max_discon

        if not root:
            return 0
        a = helper(root)
        return max(a)

    # we do not need to return max_discon, just keep it as a global variable that could be updated
    # outside helper()