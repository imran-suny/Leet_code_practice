https://leetcode.com/problems/validate-binary-search-tree/description/

class Solution:
    def isValidBST(self, root: TreeNode):    # compare with root as binary search tree//// left.node side node.value theke choto, node.val upper
        def valid(node, left, right):        # node.right > node.val-- lower 
            if not node:
                return True
            if not (left < node.val < right):                                  # -inf < node.val < +inf
                return False                               

            return valid(node.left, left, node.val) and valid( node.right, node.val, right)   
            # jake check seta first, left boundary(-inf), main mode value///
            #jake check seta first, main mode value, right boundary(+inf)

        return valid(root, float("-inf"), float("inf"))
