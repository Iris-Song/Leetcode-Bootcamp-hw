class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        stack = []
        for start,end in points:
            if stack and start<=stack[-1][1]:
                stack[-1][0]=max(start,stack[-1][0])
                stack[-1][1]=min(end,stack[-1][1])
            else:
                stack.append([start,end])
        return len(stack)