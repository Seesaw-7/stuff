class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def helper(curr: str, open:int, closed:int):
            if open == n and closed == n:
                ans.append(curr)
                return
            if open == closed:
                new_curr = curr + '('
                helper(new_curr, open+1, closed)
            elif open == n:
                new_curr = curr + ')'
                helper(new_curr, open, closed+1)               
            else:
                new_curr1 = curr + '('
                helper(new_curr1, open+1, closed)
                new_curr2 = curr + ')'
                helper(new_curr2, open, closed+1)

        helper('', 0, 0)
        return ans