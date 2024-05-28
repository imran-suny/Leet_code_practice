https://leetcode.com/problems/binary-tree-right-side-view/description/
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        queue = deque([root])
        res = []

        while queue:
            level_length = len(queue)

            for i in range(level_length):
                node = queue.popleft()
                
                if i == level_length - 1:
                    res.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return res
