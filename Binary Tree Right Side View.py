https://leetcode.com/problems/binary-tree-right-side-view/description/
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []        
        queue = deque([root])                 # q= [1, ]
        res = []

        while queue:
            level_length = len(queue)       # 1   2nd: len = 2

            for i in range(level_length):
                node = queue.popleft()             # 2 pop kolre [3] thakbe 
                
                if i == level_length - 1:   # 0= 1-1    , 0= 2-1
                    res.append(node.val)    # res = [1], 3 append hobe on 2nd loop 
                
                if node.left:               # node.left = 2 
                    queue.append(node.left) # q = [2,]
                if node.right:
                    queue.append(node.right) # q = [2, 3]  q = [4]
        return res
        
#       1
#      / \
#     2   3
#      \   \
#       5   4
