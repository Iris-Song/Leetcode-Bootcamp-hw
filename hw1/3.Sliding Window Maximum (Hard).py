class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = collections.deque()
        for i in range(k):
            while q and nums[q[-1]]<nums[i]:
                q.pop()
            q.append(i)
        res = [nums[q[0]]]
        for i in range(k,len(nums)):
            while q and nums[q[-1]]<nums[i]:
                q.pop()
            q.append(i)
            while q and i-q[0]>=k:
                q.popleft()
            res.append(nums[q[0]])
        return res