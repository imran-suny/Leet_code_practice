https://leetcode.com/problems/linked-list-cycle/description/

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow, fast = head, head

        while fast and fast.next:   # if slow and fast meet each other, then circle 
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
