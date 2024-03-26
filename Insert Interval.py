https://leetcode.com/problems/insert-interval/description/
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Insert newInterval into intervals( intervals is still sorted in ascending order) and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

If the current interval ends before the new interval starts, we continue iterating.
If the current interval starts after the new interval ends, we insert the new interval at the current position.
If there is an overlap between the current interval and the new interval, we merge them and update the new interval accordingly.

class Solution:
    def insert( self, intervals, newInterval):
        res = []
        for i in range(len(intervals)):          
            if newInterval[1] < intervals[i][0]:         #   [[1, 3], [6, 9], [11, 15]], new= [4, 5] and intervals[i] = [6, 9], we can insert [4, 5] before [6, 9]
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:       # , if newInterval = [16, 18] and intervals[i] = [11, 15], we can continue to the next interval
                res.append(intervals[i])
            else:                                              # overlap hole min , max 
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1]),
                ]
        res.append(newInterval)
        return res
