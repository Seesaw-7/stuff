class Solution:
    # Accepted, beating 9.72% in time, 24.88% in memory
    # Time complexity O(n^2)
    def lengthOfLongestSubstring_v1(self, s: str) -> int:
        max_len = 0
        for i in range(0, len(s)):
            temp = set()
            for j in range(i, len(s)):
                if s[j] in temp:
                    if len(temp) > max_len:
                        max_len = len(temp)
                    temp = set()
                    break
                else: 
                    temp.add(s[j])
                    if j == len(s) - 1:
                        if len(temp) > max_len:
                            max_len = len(temp)
        return max_len

    # Accepted, beating 95.05% in time, 5.51% in memory
    # Time complexity O(n)
    def lengthOfLongestSubstring_v2(self, s: str) -> int:
        max_len = 0
        temp = []
        for i in range(0, len(s)):
            if s[i] in temp:
                if len(temp) > max_len:
                    max_len = len(temp)
                index = temp.index(s[i])
                temp = temp[(index+1):]
            temp.append(s[i])
        if len(temp) > max_len:
            max_len = len(temp)
        return max_len

    # Improved coding style based on v2
    # 64.11%
    # The conditional check (if len(temp) > max_len) might be slightly more efficient than using the max function in lengthOfLongestSubstring. This is because the max function involves a function call and a comparison, which could be slightly more overhead than a direct comparison, especially when repeated many times in a loop.
    def lengthOfLongestSubstring_v3(self, s: str) -> int:
        max_len = 0
        temp = []
        for letter in s:
            if letter in temp:
                index = temp.index(letter)
                temp = temp[(index+1):]
            temp.append(letter)
            max_len = max(max_len, len(temp))
        return max_len 

    # The efficiency could be significantly improved by using a hash table to store the indices of characters. 
    # Use dictionary for quicker lookup, instead of list
    # Time: 99.24%
    # Space: 5.51%
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        temp = {}
        start = 0
        for i, letter in enumerate(s):
            # max_len = max(max_len, i-start+1)
            last_appearance = temp.get(letter, -1)
            if last_appearance >= start:
                start += (last_appearance-start+1)
            temp[letter] = i
            max_len = max(max_len, i-start+1)
        return max_len
            