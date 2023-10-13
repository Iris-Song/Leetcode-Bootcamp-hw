class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hasht = {}
        res = 0
        begin = 0

        for i,c in enumerate(s):
            
            if c not in hasht:
                res=max(i-begin+1,res)
            else:
                if hasht[c]>=begin:
                    res=max(i-begin-1,res)
                    begin = hasht[c]+1
                else:
                    res=max(i-begin+1,res)
            hasht[c] = i
            
        return res