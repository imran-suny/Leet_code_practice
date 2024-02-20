https://leetcode.com/problems/maximum-depth-of-binary-tree/description/ 
# RECURSIVE DFS
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))  ## 1 kore add korbe// (3) :1+ max(0, 0)= 1 

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
            q.append(root)
        level = 0
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return level
