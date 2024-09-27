from collections import Counter, defaultdict

class Solution:
    # extremely slow and clumsy
    def groupAnagrams1(self, strs: list[str]) -> list[list[str]]:
        ans = [[] for _ in range(101)]
        w_c = [{} for _ in range(101)]
        counter = [0 for _ in range(101)]

        for w in strs:
            cnt = Counter(w)
            len_w = len(w)
            flag = 0
            for i, c in enumerate(ans[len_w]):
                if cnt == w_c[len_w][i]:
                    c.append(w)
                    flag = 1
                    break
            if not flag:
                ans[len_w].append([w])
                w_c[len_w][counter[len_w]] = cnt
                counter[len_w] += 1

        res = [item for sublist in ans for item in sublist]
        return res

    # sorting and use string as the dict key
    def groupAnagrams2(self, strs: list[str]) -> list[list[str]]:
        mp = {}
        for w in strs:
            key = "".join(sorted(w))
            mp[key] = mp.get(key, [])
            mp[key].append(w)

        ans = [w for w in mp.values()]
        return ans

    # using defaultdict(list)
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        mp = defaultdict(list)
        for w in strs:
            key = "".join(sorted(w))
            mp[key].append(w)

        ans = [w for w in mp.values()]
        return ans
