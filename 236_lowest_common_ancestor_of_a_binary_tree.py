# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # Time Limit
    def lowestCommonAncestor1(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def find(node) -> int:
            if not node:
                return 0
            if node == p or node == q:
                return 1
            l = find(node.left)
            r = find(node.right)
            return l or r

        if root == p or root == q:
            if find(root.left) or find(root.right):
                return root
        l = find(root.left)
        r = find(root.right)
        if l and r:
            return root
        elif l:
            return self.lowestCommonAncestor(root.left, p, q)
        elif r:
            return self.lowestCommonAncestor(root.right, p, q)
        
    def lowestCommonAncestor2(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if root == p or root == q:
            return root
        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)
        if l and r:
            return root
        elif l:
            return l
        else:
            return r
            
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root
        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)
        if l and r:
            return root
        else:
            return l or r