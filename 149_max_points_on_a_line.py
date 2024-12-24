class Solution:
    # 12 mins O(N^3)
    def maxPoints(self, points: list[list[int]]) -> int:
        num = len(points)
        if num == 0 or num == 1:
            return num
        max_val = 2
        for i, p1 in enumerate(points):
            for j in range(i+1, num):
                p2 = points[j]
                curr = 2
                for k in range(j+1, num):
                    p3 = points[k]
                    if (p3[1] - p1[1]) == 0 and (p2[1] - p1[1]) == 0:
                        curr += 1
                        continue
                    elif (p3[1] - p1[1]) == 0 or (p2[1] - p1[1]) == 0:
                        continue
                    if (p3[0] - p1[0]) / (p3[1] - p1[1]) == (p2[0] - p1[0]) / (p2[1] - p1[1]):
                        curr += 1
                if curr > max_val:
                    max_val = curr
        return max_val

    # O(N^2)
    def maxPoints(self, points: list[list[int]]) -> int:
        num = len(points)
        if num == 0 or num == 1:
            return num
        max_num = 2
        for i, p1 in enumerate(points):
            slopes = defaultdict(int)
            vertical = 0
            for j in range(i+1, num):
                p2 = points[j]
                if p2[0] == p1[0]:
                    vertical += 1
                else:
                    slope = (p2[1] - p1[1]) / (p2[0] - p1[0])
                    slopes[slope] += 1
            curr_max = 1
            for k, v in slopes.items():
                if v > curr_max:
                    curr_max = v
            max_num = max(curr_max + 1, max_num, vertical+1)

        return max_num
