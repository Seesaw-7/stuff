class Solution:
    def isIsomorphic1(self, s: str, t: str) -> bool:
        s2t = {}
        t_new = []
        used_value = set()

        for i,c in enumerate(s):
            if t[i] in s2t:
                t_new.append(s2t[t[i]])
            else:
                if c not in used_value and t[i] not in s2t:
                    s2t[t[i]] = c
                    used_value.add(c)
                    t_new.append(c)
                else:   
                    return False

        t_new = "".join(t_new)
        return t_new == s

    # https://leetcode.com/problems/isomorphic-strings/solutions/57941/python-different-solutions-dictionary-etc/?envType=study-plan-v2&envId=top-interview-150
    def isIsomorphic2(self, s: str, t: str) -> bool:
        return len(set(zip(s,t))) == len(set(s)) == len(set(t))

    def isIsomorphic3(self, s: str, t: str) -> bool:
        return [s.find(i) for i in s] == [t.find(j) for j in t]

    def isIsomorphic(self, s: str, t: str) -> bool:
        return list(map(s.find, s)) == list(map(t.find, t))
    