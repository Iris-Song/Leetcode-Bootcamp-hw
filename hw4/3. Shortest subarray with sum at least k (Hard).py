class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        ans = math.inf
        presubsum = [0]
        for num in nums:
            presubsum.append(presubsum[-1]+num)
        q = []
        for i,curSum in enumerate(presubsum):
            while q and curSum-presubsum[q[0]]>=k:
                ans = min(ans,i-q.pop(0))
            while q and presubsum[q[-1]]>=curSum:
                q.pop()
            q.append(i)
        return ans if ans<math.inf else -1