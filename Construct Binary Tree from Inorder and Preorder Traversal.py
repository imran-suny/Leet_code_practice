https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]

consider pre= [20,15,7] in = [15, 20, 7] we know pre means root first, left, right,, so 20=root, left a 15 jabe  pre[1:mid+1]
inorder means-- left, root, right, mid = root r position inorder a , then inorder [:mid]

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder: # base  checks if  preorder or inorder list is empty.
                                        #If empty,there are no more nodes to construct, and None is returned
            return None

        root = TreeNode(preorder[0])   # root 20
        mid = inorder.index(preorder[0]) # mid = 1
        root.left = self.buildTree(preorder[1 : mid + 1], inorder[:mid])  # buildTree( pre [15], in[15])
        root.right = self.buildTree(preorder[mid + 1 :], inorder[mid + 1 :]) # buildtree (pre[7], in[7])
        return root
