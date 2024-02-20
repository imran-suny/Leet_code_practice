https://leetcode.com/problems/maximum-depth-of-binary-tree/description/ 
Input: root = [3,9,20,null,null,15,7]
Output: 3

# RECURSIVE DFS
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))      ## 1 kore add korbe// (3) :1+ max(0, 0)= 1
### 3, 9, 20 -->  1 + max( (1+ max (self.maxDepth(root.left)),  (1+ max (self.maxDepth(root.right)) )-- 1+max(1, 1)-- 1+1 =2 

# ITERATIVE DFS
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        stack = [[root, 1]]  # depth and node store in a stack 
        res = 0
        while stack:
            node, depth = stack.pop()   # pop and add if not empty node /// depth o update 

            if node:
                res = max(res, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        return res
# BFS
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        q = deque()   # add and remove simultanesoulty 
        if root:
            q.append(root) # root append 
        level = 0
        while q:                   # root empty na hole, surute pop, then add left/right, increase  level+=1
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return level
