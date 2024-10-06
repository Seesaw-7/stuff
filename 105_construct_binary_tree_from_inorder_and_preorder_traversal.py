# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # iterative with stack to take the parents of left nodes
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        stack = []
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        temp = root

        for i,val in enumerate(preorder):
            if i == 0:
                continue
            new = TreeNode(val)
            if inorder.index(val) < inorder.index(temp.val):
                stack.append(temp)
                temp.left = new
                temp = new
            else:
                if stack:
                    future_parent = stack[-1]
                    while inorder.index(val) > inorder.index(future_parent.val):
                        temp = future_parent
                        stack.pop()
                        if stack:
                            future_parent = stack[-1]
                        else:
                            break
                temp.right = new
                temp = new
        
        return root

    # recursion
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not inorder:
            return None
        nodes = set(inorder)
        for i,val in enumerate(preorder):
            if val in nodes:
                root = TreeNode(val)
                preorder = preorder[i+1:]
                break

        i = inorder.index(root.val)
        left_inorder= inorder[:i]
        right_inorder = inorder[i+1:]
        root.left = self.buildTree(preorder, left_inorder)
        root.right = self.buildTree(preorder, right_inorder)

        return root

    # recursion that takes advantage of mutable list preorder
    # all nodes in the left subtree will appear first in the preorder list, then do the nodes in the right subtree
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not inorder:
            return None
        val = preorder.pop(0)
        root = TreeNode(val)
        idx = inorder.index(val)
        root.left = self.buildTree(preorder, inorder[:idx])
        root.right = self.buildTree(preorder, inorder[idx+1:])
        return root
                    