class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        len_c = len(candidates)
        ans = []
        def helper(idx:int, curr: list[int]) -> None:
            sum_curr = sum(curr)
            if sum_curr == target:
                ans.append(curr)
                return
            elif sum_curr > target:
                return
            
            for i in range(idx, len_c):
                new_curr = curr + [candidates[i]]
                helper(i, new_curr)

        helper(0, [])
        return ans