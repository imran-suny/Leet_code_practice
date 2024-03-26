https://leetcode.com/problems/merge-intervals/description/
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda pair: pair[0])
        output = [intervals[0]]

        for start, end in intervals:
            lastEnd = output[-1][1]      #last output r scond elemtn////   # Is the end of the first interval less than the start of the second interval?   

            if start <= lastEnd:
                # merge
                output[-1][1] = max(lastEnd, end)               #[1,5] [2,4]
            else:
                output.append([start, end])                      # [1,5] [7,8] non overlaping 
        return output
