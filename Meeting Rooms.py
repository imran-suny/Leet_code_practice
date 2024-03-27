Given an array of meeting time intervals consisting of start and end times[[s1,e1],[s2,e2],...](si< ei), determine if a person could attend all meetings.
Input: [[0,30],[5,10],[15,20]]
Output: false


class Solution:
    def canAttendMeetings(self, intervals):
        intervals.sort(key=lambda i: i[0])
        for i in range(1, len(intervals)):
            i1 = intervals[i - 1]   # first
            i2 = intervals[i]       # second 

            if i1[1] > i2[0]:        #compare 
                return False
        return True


def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        new_intervals = sorted(intervals, key=lambda x: x[0])
        for i in range(1,len(new_intervals)):
            if new_intervals[i-1][1] > new_intervals[i][0]:return False
        return True
  

  
