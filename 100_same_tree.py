# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        elif p or q:
            return False
        elif p and not q:
            return False

        a = p.val == q.val
        b = self.isSameTree(p.left, q.left)
        c = self.isSameTree(p.right, q.right)
        return a and b and c

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p and q:
            a = p.val == q.val
            b = self.isSameTree(p.left, q.left)
            c = self.isSameTree(p.right, q.right)
            return a and b and c
        else:
            return not p and not q