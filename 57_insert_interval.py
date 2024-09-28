class Solution:
    def insert1(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        ans = []
        flag = 0 # whether the new interval has been inserted

        for ran in intervals:
            if not flag:
                if ran[1] < newInterval[0]:
                    ans.append(ran)
                elif ran[0] <= newInterval[0] and ran[1] >= newInterval[0]:
                    ans.append([ran[0], max(ran[1], newInterval[1])])
                    flag = 1
                elif ran[0] > newInterval[1]:
                    ans.append(newInterval)
                    ans.append(ran)
                    flag = 1
                else:
                    ans.append([min(ran[0], newInterval[0]), max(ran[1], newInterval[1])])
                    flag = 1
            else:
                if ans[-1][1] < ran[0]:
                    ans.append(ran)
                else:
                    ans[-1][1] = max(ran[1], ans[-1][1])

        if not flag:
            ans.append(newInterval)

        return ans

    # a global veiw instead of a linear scan view
    # https://leetcode.com/problems/insert-interval/solutions/21622/7-lines-3-easy-solutions/?envType=study-plan-v2&envId=top-interview-150
    def insert(self, intervals, newInterval):
        s, e = newInterval.start, newInterval.end
        left = [i for i in intervals if i.end < s]
        right = [i for i in intervals if i.start > e]
        if left + right != intervals:
            s = min(s, intervals[len(left)].start)
            e = max(e, intervals[~len(right)].end)
        return left + [s, e] + right
