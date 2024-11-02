class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        ans = []
        def helper(curr: list[int], rem: list[int]):
            if not rem:
                ans.append(curr)
                return
            for i,r in enumerate(rem):
                new_rem = rem[:i] + rem[i+1:]
                new_curr = curr + [r]
                helper(new_curr, new_rem)
        helper([], nums)
        return ans