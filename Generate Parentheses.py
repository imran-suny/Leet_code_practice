Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return

            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()

        backtrack(0, 0)
        return res



1. Add `(`: stack = ["("], openN = 1, closedN = 0
2. Add `(`: stack = ["(", "("], openN = 2, closedN = 0
3. Add `(`: stack = ["(", "(", "("], openN = 3, closedN = 0
   - No more `(` can be added because `openN == n`.

4. Add `)`: stack = ["(", "(", "(", ")"], openN = 3, closedN = 1
5. Add `)`: stack = ["(", "(", "(", ")", ")"], openN = 3, closedN = 2
6. Add `)`: stack = ["(", "(", "(", ")", ")", ")"], openN = 3, closedN = 3
   - Reached the base case, so add `"((()))"` to `res`.

7. Backtrack to: stack = ["(", "(", "(", ")", ")"], openN = 3, closedN = 2
8. Backtrack to: stack = ["(", "(", "("], openN = 3, closedN = 1
   - No more `)` to add, so pop.

9. Backtrack to: stack = ["(", "("], openN = 2, closedN = 0
   - Now add `)` instead of another `(`.

10. Add `)`: stack = ["(", "(", ")"], openN = 2, closedN = 1
11. Add `(`: stack = ["(", "(", ")", "("], openN = 3, closedN = 1
12. Add `)`: stack = ["(", "(", ")", "(", ")"], openN = 3, closedN = 2
13. Add `)`: stack = ["(", "(", ")", "(", ")", ")"], openN = 3, closedN = 3
    - Reached the base case, so add `"(()())"` to `res`.

14. Backtrack to: stack = ["(", "(", ")", "(", ")"], openN = 3, closedN = 2
15. Backtrack to: stack = ["(", "(", ")", "("], openN = 3, closedN = 1
16. Backtrack to: stack = ["(", "(", ")"], openN = 2, closedN = 1
   - No more `)` to add, so pop.

17. Backtrack to: stack = ["(", "("], openN = 2, closedN = 0
18. Add `)`: stack = ["(", ")", "("], openN = 2, closedN = 1
19. Add `(`: stack = ["(", ")", "(", "("], openN = 3, closedN = 1
20. Add `)`: stack = ["(", ")", "(", "(", ")"], openN = 3, closedN = 2
21. Add `)`: stack = ["(", ")", "(", "(", ")", ")"], openN = 3, closedN = 3
    - Reached the base case, so add `"(())()"` to `res`.

22. Backtrack to: stack = ["(", ")", "(", "(", ")"], openN = 3, closedN = 2
23. Backtrack to: stack = ["(", ")", "(", "("], openN = 3, closedN = 1
24. Backtrack to: stack = ["(", ")", "("], openN = 2, closedN = 1
   - No more `)` to add, so pop.

25. Backtrack to: stack = ["(", ")", "("], openN = 1, closedN = 1
26. Add `)`: stack = ["(", ")", "(", ")"], openN = 2, closedN = 2
27. Add `(`: stack = ["(", ")", "(", ")", "("], openN = 3, closedN = 2
28. Add `)`: stack = ["(", ")", "(", ")", "(", ")"], openN = 3, closedN = 3
    - Reached the base case, so add `"()(())"` to `res`.

29. Backtrack to: stack = ["(", ")", "(", ")", "("], openN = 3, closedN = 2
30. Backtrack to: stack = ["(", ")", "(", ")"], openN = 2, closedN = 2
31. Backtrack to: stack = ["(", ")", "("], openN = 1, closedN = 1
   - No more `)` to add, so pop.

32. Backtrack to: stack = ["(", ")"], openN = 1, closedN = 0
33. Add `(`: stack = ["(", ")", "("], openN = 2, closedN = 1
34. Add `)`: stack = ["(", ")", "(", ")"], openN = 2, closedN = 2
35. Add `(`: stack = ["(", ")", "(", ")", "("], openN = 3, closedN = 2
36. Add `)`: stack = ["(", ")", "(", ")", "(", ")"], openN = 3, closedN = 3
    - Reached the base case, so add `"()()()"` to `res`.

