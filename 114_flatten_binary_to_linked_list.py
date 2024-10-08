# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def helper(node):
            if not node:
                return node
            if not node.left and not node.right:
                return node
            l = node.left
            r = node.right
            node.left = None
            if l:
                node.right = l
                newnode = helper(node.right)
                if r:
                    newnode.right = r
                    newnode = helper(newnode.right)
                return newnode
            else:
                node.right = r
                newnode = helper(node.right)
                return newnode
        
        helper(root)