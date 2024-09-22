class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        curr_w = 0 # currant width, minus one extra space
        curr_num = 0 # currant number of words
        curr_list = [] # currant word list in this line
        ans = []

        for i,w in enumerate(words):
            if curr_w + len(w) + curr_num <= maxWidth:
                curr_w += len(w)
                curr_num += 1
                curr_list.append(w)
            else:
                if curr_num == 1:
                    curr_line = curr_list[0] + " "*(maxWidth-curr_w)
                else:
                    every = (maxWidth - curr_w) // (curr_num - 1)
                    more = (maxWidth - curr_w) % (curr_num - 1)
                    curr_line = ""
                    if more > 0:
                        curr_line = (" "*(every+1)).join(curr_list[:more]) + " "*(every+1)
                    curr_line += (" "*(every)).join(curr_list[more:])
                ans.append(curr_line)
                curr_w = len(w)
                curr_num = 1
                curr_list = [w]
            if i == len(words) - 1:
                curr_line = " ".join(curr_list) + " "*(maxWidth-(curr_w+curr_num-1))
                ans.append(curr_line)
                return ans
        return ans
