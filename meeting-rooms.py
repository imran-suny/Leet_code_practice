https://aaronice.gitbook.io/lintcode/sweep-line/meeting-rooms

Input:
[[0,30],[5,10],[15,20]]
Output:
 false
Input:
 [[7,10],[2,4]]
Output:
 true


class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """
    def canAttendMeetings(self, intervals):
        intervals.sort(key=lambda i: i[0])

        for i in range(1, len(intervals)):
            i1 = intervals[i - 1]
            i2 = intervals[i]

            if i1[1] > i2[0]:  30>5
                return False
        return True

