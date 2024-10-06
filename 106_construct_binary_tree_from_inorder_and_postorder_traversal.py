# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder:
            return None
        root_val = postorder.pop()
        root = TreeNode(root_val)
        idx = inorder.index(root_val)
        root.right = self.buildTree(inorder[idx+1:], postorder)
        root.left = self.buildTree(inorder[:idx], postorder)
        return root
    
    # A simple iteration with stack can also be done by linearly scanning the postorderlist from right to left