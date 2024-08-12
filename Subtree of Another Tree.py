class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not t:   # subtree null hole true, cause main tree te null thakbe 
            return True
        if not s:   # main tree empty hole False
            return False
        if self.sameTree(s, t):   # root same kina ?
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)    # s.left / s.right kina ??

    def sameTree(self, s, t):
        if not s and not t:
            return True
        if s and t and s.val == t.val:
            return self.sameTree(s.left, t.left) and self.sameTree(s.right, t.right)
        return False
