class Solution:
    # fastest
    def reverseWords1(self, s: str) -> str:
        list_words = s.strip().split(' ')
        list_words.reverse()
        result = list_words[0]
        for i in range(1, len(list_words)):
            if list_words[i] != '' :
                result += ' '
                result += list_words[i]
        return result

    def reverseWords2(self, s: str) -> str:
        list_words = s.strip().split(' ')
        list_words.reverse()
        reverse = [x for x in list_words if x != '']
        return " ".join(reverse)

    # built-in
    def reverseWords3(self, s: str) -> str:
        list_words = s.split() # automatically splits words and handles multi-spaces
        list_words.reverse()
        return " ".join(list_words)

    # non-built-in
    def reverseWords(self, s: str) -> str:
        list_words = []
        flag = 0

        s += ' '
        words = ''
        for c in s:
            if c != ' ':
                if flag == 0:
                    flag = 1
                    words = c
                else:
                    words += c
            else:
                if flag == 1:
                    flag = 0
                    list_words.append(words)
                    words = ''

        mid = len(list_words) // 2
        for i in range(0, mid):
            list_words[i], list_words[-i-1] = list_words[-i-1], list_words[i]

        result = list_words[0]
        for i in range(1, len(list_words)):
            if list_words[i] != '' :
                result += ' '
                result += list_words[i]
        return result
