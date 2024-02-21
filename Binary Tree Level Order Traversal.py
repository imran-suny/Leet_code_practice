https://leetcode.com/problems/binary-tree-level-order-traversal/solutions/4688444/52-1-approach-1-o-n-python-c-step-by-step-explanation/

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []    ## [   [] ], so need 2 of these
        q = collections.deque()
        if root:
            q.append(root)

        while q:
            val = []

            for i in range(len(q)):   ### queqe te jotogula ache, so gula check korbo 
                node = q.popleft() # 1ta remove
                val.append(node.val) # sathe sathe add value in 2nd [] te 
                if node.left:   # if any left node, then append in the queue
                    q.append(node.left)
                if node.right:  # if right, append 
                    q.append(node.right)
            res.append(val)  # apppend the 1st  [ [], [ ] ]
        return res
