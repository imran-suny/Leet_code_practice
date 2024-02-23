https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []  # stack for append and pop, append when there is a subtree, Null hole pop()
        curr = root  # temp as there is left and right and while to continue loop 

        while stack or curr:   # left/right sesh na hole ans stack empty na hole
            while curr:
                stack.append(curr)
                curr = curr.left  # In order, so left a jetei thakbo--then root, then right
            curr = stack.pop()  # curr- Null hole pop
            k -= 1
            if k == 0:
                return curr.val
            curr = curr.right  # left sesh hole right a 
