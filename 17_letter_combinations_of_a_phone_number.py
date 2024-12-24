class Solution:
    # iteration
    def letterCombinations1(self, digits: str) -> List[str]:
        com = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv","9":"wxyz"}
        if not digits:
            return []
        ans = [""]
        
        for d in digits:
            new_ans = []
            for a in ans:
                for c in com[d]:
                    new_a = a + c
                    new_ans.append(new_a)
            ans = new_ans
        
        ans = ["".join(x) for x in ans]

        return ans

    # recursion
    def letterCombinations2(self, digits: str) -> List[str]:
        d = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        def helper(digits: str, prev):
            if not digits:
                return []
            new_prev = []
            for p in prev:
                for c in d[digits[0]]:
                    new_prev.append(p+c)
            if len(digits) == 1:
                return new_prev
            else:
                return helper(digits[1:], new_prev)

        return helper(digits, [""])

    # backtrack
    def letterCombinations(self, digits: str) -> List[str]:
        d = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
        def helper(digits: str):
            res = []
            if not digits:
                return []
            if len(digits) == 1:
                for c in d[digits[0]]:
                    res.append(c)
                return res
            for c in d[digits[0]]:
                for string in helper(digits[1:]):
                    res.append(c+string)
            return res

        return helper(digits)

    # backtrack with dfs       
    def letterCombinations(self, digits: str) -> List[str]:
        d = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        res = []
        if not digits:
            return []

        def helper(idx: int, path):
            if idx == len(digits):
                res.append(path)
                return
            for c in d[digits[idx]]:
                helper(idx+1, path+c)

        helper(0, '')
        return res