
class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        while True:
            if root.val < p.val and root.val < q.val:    # right a move
                root = root.right
            elif root.val > p.val and root.val > q.val:
                root = root.left
            else:                                ## otther case a roo return (right right/ left a sore jabe)
                return root
