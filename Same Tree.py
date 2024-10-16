https://leetcode.com/problems/same-tree/description/

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:  # root not same, False
            return True
        if p and q and p.val == q.val:    ## p and q not empty and value is same, check 
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return False
