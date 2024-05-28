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
                node = queue.popleft()             #  [1] pop korle [], 2nd iterationa, 2 pop kolre [3] thakbe 
                
                if i == level_length - 1:   # 0= 1-1    , 0= 2-1
                    res.append(node.val)    # res = [1], 3 append hobe on 2nd loop 
                
                if node.left:               # node.left = 2 
                    queue.append(node.left) # q = [2,]
                if node.right:
                    queue.append(node.right) # q = [2, 3] ,  q = [3,5]
        return res
        
#       1
#      / \
#     2   3
#      \   \
#       5   4

queue = deque([root]) initializes a queue with the root node [1].
res = [] initializes an empty list to store the result.
    
level_length = len(queue) sets level_length to 1 because there is only one node at this level.
for i in range(level_length): starts a loop that will iterate 1 time.
First For Loop (Processing Node 1):
node = queue.popleft() removes and returns the first node from the queue, which is 1. Now, queue is [].
if i == level_length - 1: checks if the current node is the last node in this level. Since i == 0 and level_length - 1 == 0, it appends 1 to res, so res = [1].
if node.left: checks if the current node has a left child. It does, so queue.append(node.left) appends 2 to queue. Now, queue is [2].
if node.right: checks if the current node has a right child. It does, so queue.append(node.right) appends 3 to queue. Now, queue is [2, 3].
Second Level:
Second While Loop:

level_length = len(queue) sets level_length to 2 because there are two nodes at this level.
for i in range(level_length): starts a loop that will iterate 2 times.
First For Loop (Processing Node 2):

node = queue.popleft() removes and returns the first node from the queue, which is 2. Now, queue is [3].
if i == level_length - 1: checks if the current node is the last node in this level. Since i == 0 and level_length - 1 == 1, it does not append 2 to res.
if node.left: checks if the current node has a left child. It does not.
if node.right: checks if the current node has a right child. It does, so queue.append(node.right) appends 5 to queue. Now, queue is [3, 5].
Second For Loop (Processing Node 3):

node = queue.popleft() removes and returns the first node from the queue, which is 3. Now, queue is [5].
if i == level_length - 1: checks if the current node is the last node in this level. Since i == 1 and level_length - 1 == 1, it appends 3 to res, so res = [1, 3].
if node.left: checks if the current node has a left child. It does not.
if node.right: checks if the current node has a right child. It does, so queue.append(node.right) appends 4 to queue. Now, queue is [5, 4].
Third Level:
Third While Loop:

level_length = len(queue) sets level_length to 2 because there are two nodes at this level.
for i in range(level_length): starts a loop that will iterate 2 times.
First For Loop (Processing Node 5):

node = queue.popleft() removes and returns the first node from the queue, which is 5. Now, queue is [4].
if i == level_length - 1: checks if the current node is the last node in this level. Since i == 0 and level_length - 1 == 1, it does not append 5 to res.
if node.left: checks if the current node has a left child. It does not.
if node.right: checks if the current node has a right child. It does not.
Second For Loop (Processing Node 4):

node = queue.popleft() removes and returns the first node from the queue, which is 4. Now, queue is [].
if i == level_length - 1: checks if the current node is the last node in this level. Since i == 1 and level_length - 1 == 1, it appends 4 to res, so res = [1, 3, 4].
if node.left: checks if the current node has a left child. It does not.
if node.right: checks if the current node has a right child. It does not.
End of Loop:
End of While Loop:
The queue is now empty, so the while loop ends.
The method returns the result list res, which is [1, 3, 4]
