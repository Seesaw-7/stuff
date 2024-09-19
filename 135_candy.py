class Solution:
    def candy(self, ratings: list[int]) -> int:
        n = len(ratings)
        answer = [1 for _ in range(n)]

        for i in range(n-1):
            if ratings[i+1] > ratings[i]:
                answer[i+1] = answer[i] + 1

        for i in reversed(list(range(n-1))):
            if ratings[i] > ratings[i+1] and answer[i] <= answer[i+1]:
                answer[i] = answer[i+1] + 1

        return sum(answer)
