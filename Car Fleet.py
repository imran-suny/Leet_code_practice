Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
Output: 3
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)] # [(10, 2), (8, 4), (0, 1), (5, 1), (3, 3)]
        pair.sort(reverse=True) # [(10, 2), (8, 4), (5, 1), (3, 3), (0, 1)]
        stack = []
        for p, s in pair:  # Reverse Sorted Order
            stack.append((target - p) / s) # (12 - 10) / 2 = 1.0, Stack: [1.0], [1.0, 1.0] pop the last element 8 r ta
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop() # Stack: [1.0, 7.0, 3.0], stack[-1] <= stack[-2] pop the last element.Stack: [1.0, 7.0]
        return len(stack)
