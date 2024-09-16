class Solution:

    # brute force O(N^2)
    def hIndex1(self, citations: list[int]) -> int:
        h_index = 0
        num_paper_satisfied = len(citations)

        while num_paper_satisfied >= h_index:
            h_index += 1
            num_paper_satisfied = 0
            for cit in citations:
                if cit >= h_index:
                    num_paper_satisfied += 1

        return h_index - 1

    # sorting, O(NlogN)
    def hIndex2(self, citations: list[int]) -> int:
        citations.sort(reverse=True)

        for i,cit in enumerate(citations):
            if cit < i+1:
                return i

        return len(citations)

    # counting O(N)
    def hIndex3(self, citations: list[int]) -> int:
        len_citations = len(citations)
        counts = [0 for _ in range(len_citations)]

        for i,num in enumerate(citations):
            if num > len_citations:
                counts[len_citations-1] += 1
            else:
                if num > 0:
                    counts[num-1] += 1

        if counts == [0 for _ in range(len_citations)]:
            return 0

        num_papers = counts[-1]

        i = len_citations - 1
        while num_papers < i+1 and i > 0:
            num_papers += counts[i-1]
            i-= 1

        return i+1

    # seems that it's way faster, though also O(N)
    def hIndex(self, citations: list[int]) -> int:
        n = len(citations)
        temp = [0 for _ in range(n + 1)]

        for i,v in enumerate(citations):
            if v > n :
                temp[n] += 1
            else:
                temp[v] += 1
        
        total = 0
        for i in range(n, -1, -1):
            total += temp[i]
            if total >= i:
                return i
                