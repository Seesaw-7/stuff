# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# O(N) space
class BSTIterator1:

    def __init__(self, root: Optional[TreeNode]):
        self.plain = []
        def helper(node:Optional[TreeNode]):
            if not node:
                return
            helper(node.left)
            if not self.plain:
                self.plain = [node.val - 1]
            self.plain.append(node.val)
            helper(node.right)
        helper(root)
        self.it = 0
        

    def next(self) -> int:
        if self.hasNext():
            self.it += 1
            return self.plain[self.it]

    def hasNext(self) -> bool:
        return self.it != len(self.plain) - 1

# O(h) space with stack
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.it = root
        while self.it.left:
            temp = self.it.left
            self.it.left = None
            self.stack.append(self.it)
            self.it = temp
        init = TreeNode(self.it.val-1)
        self.stack.append(self.it)
        self.it = init

    def next(self) -> int:
        if not self.it.left and not self.it.right:
            self.it = self.stack.pop()
            return self.it.val
        elif not self.it.left:
            self.it = self.it.right
            while self.it.left:
                temp = self.it.left
                self.it.left = None
                self.stack.append(self.it)
                self.it = temp
            return self.it.val

    def hasNext(self) -> bool:
        return True if self.it.right or self.stack else False

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()