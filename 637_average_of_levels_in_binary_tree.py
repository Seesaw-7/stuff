# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        ans = []
        nodes = deque()
        nodes.append((root, 0))
        sumlevel = 0
        numlevel = 0
        while nodes:
            curr, l = nodes.popleft()
            if curr.left:
                nodes.append((curr.left, l+1))
            if curr.right:
                nodes.append((curr.right, l+1))
            if l > len(ans):
                ans.append(sumlevel/numlevel)
                sumlevel = curr.val
                numlevel = 1
            else:
                sumlevel += curr.val
                numlevel += 1

        ans.append(sumlevel/numlevel)
        return ans


