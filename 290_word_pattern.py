class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        return len(s) == len(pattern) and len(set(zip(pattern, s))) == len(set(pattern)) == len(set(s))
