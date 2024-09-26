from collections import deque, Counter

class Solution:
    def findSubstring1(self, s: str, words: list[str]) -> list[int]:
        win_size = len(words[0])
        num_words = len(words)
        word_set = set(words)
        valid = deque()
        cnt = Counter(words)
        not_appeared = cnt.copy()
        i = 0
        ans = []

        for _ in range(win_size):
            while i < len(s):
                curr = s[i:i+win_size]
                if curr in word_set:
                    if curr in not_appeared and not_appeared[curr] > 0:
                        not_appeared[curr] -= 1
                        valid.append(curr)
                    else:
                        item = valid.popleft()
                        while valid and item != curr:
                            not_appeared[item] += 1
                            item = valid.popleft()
                        valid.append(curr)
                    i += win_size
                else:
                    not_appeared = cnt.copy()
                    valid = deque()
                    i += 1
                if len(valid) == num_words:
                    item = valid.popleft()
                    not_appeared[item] += 1
                    ans.append(i - num_words * win_size)
            s = s[1:]
        return ans               


    # 受不了了，我要开始brute force
    # 最复杂的题目，往往只需要最朴素的处理方式
    def findSubstring2(self, s: str, words: list[str]) -> list[int]:
        len_word = len(words[0])
        num_words = len(words)
        len_con = len_word * num_words
        cnt = Counter(words)
        ans = []
        okay = set()
        
        for i in range(len(s)-len_con+1):
            con = s[i:i+len_con]
            if con in okay:
                ans.append(i)
                continue
            c = cnt.copy()
            targeted = 0
            j = 0
            for j in range(0, len_con, len_word):
                curr = con[j:j+len_word]
                if curr in c:
                    if c[curr] > 0:
                        c[curr] -= 1
                        targeted += 1
                    else:
                        break
                else:
                    break
                j += len_word
            if targeted == num_words:
                ans.append(i)
                okay.add(con)

        return ans

    # avoid long slicings
    def findSubstring3(self, s: str, words: list[str]) -> list[int]:
        len_word = len(words[0])
        num_words = len(words)
        len_con = len_word * num_words
        word_count = Counter(words)
        ans = []
        
        for i in range(len(s) - len_con + 1):
            seen_words = Counter()
            matched_words = 0
            
            for j in range(0, len_con, len_word):
                curr_word = s[i + j:i + j + len_word]
                
                if curr_word in word_count:
                    seen_words[curr_word] += 1
                    
                    if seen_words[curr_word] > word_count[curr_word]:
                        break
                    matched_words += 1
                else:
                    break
            
            if matched_words == num_words:
                ans.append(i)
        
        return ans

    # only scan `window_size` times
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        win_size = len(words[0])
        num_words = len(words)
        word_set = set(words)
        valid = deque()
        cnt = Counter(words)
        not_appeared = cnt.copy()
        i = 0
        ans = []

        for _ in range(win_size):
            while i < len(s):
                curr = s[i:i+win_size]
                if curr in word_set:
                    if curr in not_appeared and not_appeared[curr] > 0:
                        not_appeared[curr] -= 1
                        valid.append(curr)
                    else:
                        item = valid.popleft()
                        while valid and item != curr:
                            not_appeared[item] += 1
                            item = valid.popleft()
                        valid.append(curr)
                else:
                    not_appeared = cnt.copy()
                    valid = deque()
                i += win_size
                if len(valid) == num_words:
                    item = valid.popleft()
                    not_appeared[item] += 1
                    ans.append(i - num_words * win_size)
            s = s[1:]
        return ans 