class Solution:
    def minWindow(self, s: str, t: str) -> str:
        mpt = collections.defaultdict(int)
        for c in t:
            mpt[c]+=1
        cntNeed = len(t)
        res = (0,float('inf'))
        i=0
        for j,c in enumerate(s):
            if mpt[c]>0:
                cntNeed-=1
            mpt[c]-=1
            if cntNeed==0:
                while True:
                    if mpt[s[i]]==0:
                        break
                    mpt[s[i]]+=1
                    i+=1
                if res[1]-res[0]>j-i:
                    res=(i,j)
                mpt[s[i]]+=1
                i+=1
                cntNeed+=1
        return '' if res[1]>len(s) else s[res[0]:res[1]+1]

        
        