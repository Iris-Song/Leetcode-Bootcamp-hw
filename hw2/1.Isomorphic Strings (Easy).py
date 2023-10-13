class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hasht = dict()
        hashs = dict()
        for i in range(len(s)):
            if s[i] not in hasht and t[i] not in hashs:
                hasht[s[i]] = t[i]
                hashs[t[i]] = s[i]
            elif s[i] in hasht and t[i] in hashs:
                if hasht[s[i]] != t[i] or hashs[t[i]] != s[i]:
                    return False
            else:
                return False
        return True
            