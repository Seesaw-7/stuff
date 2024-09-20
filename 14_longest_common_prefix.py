class Solution:
    def longestCommonPrefix1(self, strs: List[str]) -> str:
        common = strs[0]

        for s in strs:
            while not s.startswith(common):
                common = common[:-1]

        return common

    # Divide and conquer, copied from lc solutions
    # https://leetcode.com/problems/longest-common-prefix/solutions/3224599/easy-and-simple-way-to-find-longest-common-prefix-python-3/?envType=study-plan-v2&envId=top-interview-150
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) <= 1:
            return strs[0]
        low = 0
        high = len(strs)
        mid = (low + high) // 2
        left = self.longestCommonPrefix(strs[:mid])
        right = self.longestCommonPrefix(strs[mid:])
        return self.findLcp(left, right)


    def findLcp(self, left, right):
        lcp = ""
        j = 0
        while j < len(left) and j < len(right):
            if left[j] == right[j]:
                lcp += left[j]
            else:
                break
            j += 1
        return lcp
