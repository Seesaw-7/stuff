class Solution:
    # effectively the maximum number of non-overlapping intervals
    # first sort the intervals according to their left end,
    # then we favor to replace the interval with a shorter right end to the non_overlap list,
    # because they can potentially accomodate more non-overlapping intervals
    # always greedily shooting where most intervals overlap is not globally optimal
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        non_overlap = []
        points.sort()

        for ran in points:
            if not non_overlap or ran[0] > non_overlap[-1][1]:
                non_overlap.append(ran)
            elif ran[1] < non_overlap[-1][1]:
                non_overlap[-1][1] = ran[1]

        return len(non_overlap)

    # actually we only need to keep track of the end and a counter, instead of a whole list
