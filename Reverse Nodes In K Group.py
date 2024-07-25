https://leetcode.com/problems/reverse-nodes-in-k-group/description/
https://leetcode.com/problems/reverse-nodes-in-k-group/solutions/4672340/44-1-approach-1-o-n-python-c-step-by-step-explanation/
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(0, head)      #  reversing the  group
        groupPrev = dummy              # groupPrev is initialized to point to the dummy node

        while True:              # The loop continues until there are no more groups of k nodes to reverse.
            kth = self.getKth(groupPrev, k)
            if not kth:     # kth is k-th node from groupPrev. If fewer than k nodes remaining, kth will be None, and the loop breaks.
                break
            groupNext = kth.next   # next group is the node following kth

            # reverse group
            prev, curr = kth.next, groupPrev.next   # kth.next re last pointer 1>2>3, curr is first node of current group[dummy.next=1]
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
                
           # Connect the reversed group to the rest of the list.
            tmp = groupPrev.next 
            groupPrev.next = kth           #updated to point to the new head of the reversed group (kth)
            groupPrev = tmp                #  updated to point to the last node of the reversed group (tmp)
        return dummy.next

    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
