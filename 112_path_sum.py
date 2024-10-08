# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def helper(node, curr_sum, targetSum):
            if not node:
                return curr_sum
            curr_sum += node.val
            suml = helper(node.left, curr_sum, targetSum)
            sumr = helper(node.right, curr_sum, targetSum)
            if not node.left and not node.right:
                return curr_sum
            elif not node.left:
                return sumr
            elif not node.right:
                return suml
            if suml == targetSum or sumr == targetSum:
                return targetSum
            else:
                return suml

        if not root:
            return False
        return targetSum == helper(root, 0, targetSum)

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
            if not root:
                return False
            targetSum -= root.val
            if not root.left and not root.right:
                return targetSum == 0
            return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)