https://leetcode.com/problems/non-overlapping-intervals/description/
Given an array of intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.
Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()          # [1,2],[1,3],[2,3],[3,4]
        res = 0
        ref = intervals[0][1]           
        for start, end in intervals[1:]:
            if start >= ref:          # [1,2],[2,3],[3,4]
                ref = end
            else:
                res += 1
                ref = min(end, ref)
        return res
