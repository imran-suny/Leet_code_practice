Given an array of meeting time intervals consisting of start and end times[[s1,e1],[s2,e2],...](si< ei), find the minimum number of conference rooms required.
Input: [[0, 30],[5, 10],[15, 20]]
Output: 2

def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        time = []
        for start, end in intervals:
            time.append((start, 1))
            time.append((end, -1))                 # [(0, 1), (30, -1), (5, 1), (10, -1), (15, 1), (20, -1)]
        
        time.sort(key=lambda x: (x[0], x[1]))      # [(0, 1), (5, 1), (10, -1), (15, 1), (20, -1), (30, -1)]  # start hole 1, end hole 0
        
        count = 0
        max_count = 0
        for t in time:                               
            count += t[1]                           #1, 2, 0,1,0,-1
            max_count = max(max_count, count)       # 1,2,2,2,2,2
        return max_count


class Solution:
  def minMeetingRooms(self, intervals: List[List[int]]) -> int:
    n = len(intervals)
    ans = 0
    starts = []
    ends = []
    for start, end in intervals:
      starts.append(start)
      ends.append(end)
    starts.sort()  # [0, 5, 15]
    ends.sort()    # [10, 20, 30]
    j = 0
    for i in range(n):
      if starts[i] < ends[j]:   # sratrt time end time theke kom, mane room lagbe 
        ans += 1
      else:
        j += 1   # update ends if no overlap 
    return ans

