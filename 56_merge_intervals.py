class Solution:
    def merge1(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        ans = []
        temp = intervals[0]
        max_end = intervals[0][1]

        for i in range(1, len(intervals)):
            if intervals[i][0] <= max_end:
                max_end = max(max_end, intervals[i][1])
                temp[1] = max_end
            else:
                max_end = intervals[i][1]
                ans.append(temp)
                temp = intervals[i]

        ans.append(temp)
        return ans

    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        ans = []

        for ran in intervals:
            if not ans or ans[-1][1] < ran[0]:
                ans.append(ran)
            else:
                ans[-1][1] = max(ans[-1][1], ran[1])

        return ans
