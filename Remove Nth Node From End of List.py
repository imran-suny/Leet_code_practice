https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)  # Step 1: Create a dummy node that points to the head of the list.
        left = dummy   # dummy 1 ta age /// na hole delete kora jabe na next.next
        right = head

        while n > 0:             # 1>2>3>4----1>2>4    # n=1 , r= 2, # Step 2: Move the right pointer n steps ahead.
            right = right.next   # left and right r distance hobe n, or 2 here    left=0, right= 2
            n -= 1

        while right:       #  # Step 3: Move both pointers until the right pointer reaches the end.        
            left = left.next     # l= 1,2
            right = right.next   # r= 3,4

        # # Step 4: Delete the target node by skipping it.
        left.next = left.next.next  # 3--delete
        return dummy.next      # 1 theke return 
