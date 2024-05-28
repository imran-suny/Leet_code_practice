https://leetcode.com/problems/balanced-binary-tree/description/

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:                                      #  if current node is None
                return [True, 0]

            left, right = dfs(root.left), dfs(root.right)
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
            return [balanced, 1 + max(left[1], right[1])]

        return dfs(root)[0]

Calculate whether the current subtree is balanced by checking if both left[0] and right[0] are True, and 
if the absolute difference between left[1] (the height of the left subtree) and right[1] (the height of the right subtree) is at most 1
