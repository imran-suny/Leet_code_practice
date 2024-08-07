https://leetcode.com/problems/largest-rectangle-in-histogram/description/
pop: Remove and return the top element of the stack.
push: Add an element to the top of the stack   
stack[-1]: View the top element of the stack without removing it.

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []  # pair: (index, height)

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index)) # calculate width of rectangle by subtracting starting index  from current index.
                start = index  # Push the current bar's index
            stack.append((start, h))
            
#After processing all bars, there may still be bars left in the stack. For each remaining bar in the stack,
#calculate the area using the height of the bar and the difference between the current index and the index at the top of the stack.
        
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea
