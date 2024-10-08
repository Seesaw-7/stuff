# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def helper(node, num):
            if not node:
                return 0
            str_num = num + str(node.val)
            if not node.left and not node.right:
                return str_num
            res = 0
            if node.left:
                res += int(helper(node.left, str_num))
            if node.right:
                res += int(helper(node.right, str_num))
            return res

        return int(helper(root, ""))