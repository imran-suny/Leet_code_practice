https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)
        left = dummy
        right = head

        while n > 0:             # 1>2>3>4----1>2>4    # n=1 , r= 2,                 #### traverse left before target node so use while
            right = right.next   # left and right r distance hobe n, or 2 here    left=0, right= 2
            n -= 1

        while right:              
            left = left.next     # l= 1,2
            right = right.next   # r= 3,4

        # delete
        left.next = left.next.next  # 3--delete
        return dummy.next      # 1 theke return 
