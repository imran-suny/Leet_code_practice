Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
# iteratively
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr = None, head     # 2 pointer curr= head, first one is head 

        while curr:                 # not empty 
            temp = curr.next        # ekta temp varibale to save the value  (2)
            curr.next = prev        # curr.next= direction reverse (1)er, null er dike
            prev = curr             # update pointer prev= curr, curr=  temp
            curr = temp
        return prev

  Recursively:
class Solution:
    def reverse(self, head: ListNode): #  function is called with the head node pointing to 1.
        if not head:
          return None
          
        newHead = head   # head diye suru always 
         if head.next:
           newHead= self.reverse (head.next) # head is not None and it has a next node (2),...5, 
           head.next.next = head #  it doesn't have a next node, it returns the head itself (i.e., 2) back up the recursion stac
         head.next = None
      return newHead
