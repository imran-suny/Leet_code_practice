https://leetcode.com/problems/reverse-nodes-in-k-group/description/
https://leetcode.com/problems/reverse-nodes-in-k-group/solutions/4672340/44-1-approach-1-o-n-python-c-step-by-step-explanation/
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(0, head)     
        groupPrev = dummy                                  # groupPrev is  dummy node

        while True:                                        # loop continues until no more groups of k
            kth = self.getKth(groupPrev, k)
            if not kth:                                     # kth node from groupPrev. If fewer than k nodes remaining, the loop breaks.
                break
            groupNext = kth.next                             # next group is the node following kth

            # reverse group
            prev, curr = kth.next, groupPrev.next   # kth.next re last pointer 1>2>3, curr is first node of current group[dummy.next=1]
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
                
           # Updating Pointers After Reversing//// Connect the reversed group to the rest of the list.
            tmp = groupPrev.next                     # first node of the current k-group.
            groupPrev.next = kth                     # dum 0>1>2, groupprev=dummy, groupprev.next =1, 0>2>1-->point-->kth  
            groupPrev = tmp                          #  groupPrev is then updated to tmp (1), which is the last node of the reversed group.
        return dummy.next

    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
