https://leetcode.com/problems/copy-list-with-random-pointer/description/
Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

class Solution:
    def copyRandomList(self, head: "Node") -> "Node":
        oldToCopy = {None: None}   # cur jokhon null hobe, last one # a hashmap map to map the original nodes to their corresponding new nodes.

        cur = head
        while cur:
            copy = Node(cur.val)   # creating new nodes for each original node 
            oldToCopy[cur] = copy  # updating the map with the mapping between original and new nodes.
            cur = cur.next
        cur = head
        while cur:
            copy = oldToCopy[cur]  # update the next and random pointers of the new nodes using the information stored in map
            copy.next = oldToCopy[cur.next]
            copy.random = oldToCopy[cur.random]
            cur = cur.next
        return oldToCopy[head]     # Return the new head of the linked list, which is the node corresponding to the original head in the map.

