# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Space Complexity O(h) cuz it's DFS, and h is the height of the tree
    # Time complexity O(N) cuz traversing
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def isSymm(left, right) -> bool:
            if left and right:
                a = left.val == right.val
                b = isSymm(left.left, right.right)
                c = isSymm(left.right, right.left)
                return a and b and c
            return not left and not right

        return isSymm(root.left, root.right) if root else True