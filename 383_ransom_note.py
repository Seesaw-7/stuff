from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag = Counter(magazine)
        ransom = Counter(ransomNote)
        return mag >= ransom
        # can also use mag - ransom
    