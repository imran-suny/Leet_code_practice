https://leetcode.com/problems/copy-list-with-random-pointer/description/
Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

class Solution:
    def copyRandomList(self, head: "Node") -> "Node":
        oldToCopy = {None: None} # cur jokhon null hobe, last one 

        cur = head
        while cur:
            copy = Node(cur.val)
            oldToCopy[cur] = copy
            cur = cur.next
        cur = head
        while cur:
            copy = oldToCopy[cur]
            copy.next = oldToCopy[cur.next]
            copy.random = oldToCopy[cur.random]
            cur = cur.next
        return oldToCopy[head]

1. Create a hashmap map to map the original nodes to their corresponding new nodes. Initialize it with None: None.
2. Traverse the original linked list while creating new nodes for each original node and updating the map with the mapping between original and new nodes.
3. Traverse the original linked list again and update the next and random pointers of the new nodes using the information stored in mapp.
4. Return the new head of the linked list, which is the node corresponding to the original head in the map.
