class Solution:
    # sliding window
    def strStr1(self, haystack: str, needle: str) -> int:
        len_needle = len(needle)
        for i in range(len(haystack)-len_needle+1):
            if haystack[i:i+len_needle] == needle:
                return i

        return -1

    # candidate elimination
    def strStr(self, haystack: str, needle: str) -> int:
        len_haystack = len(haystack)
        len_needle = len(needle)
        possible = [i for i in range(len_haystack)]

        for i in range(len_needle):
            if not possible:
                return -1
            possible = [x for x in possible if x+i < len_haystack and haystack[x+i] == needle[i]]

        return possible[0] if possible else -1
