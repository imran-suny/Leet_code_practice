Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
# iteratively
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr = None, head     # 2 pointer curr= head, first one is head 

        while curr:                 # not empty 
            temp = curr.next        # ekta temp varibale to save the value  (2)
            curr.next = prev        # curr.next= direction reverse (2)er
            prev = curr             # update pointer prev= curr, curr=  temp
            curr = temp
        return prev

  Recursively:
class Solution:
    def reverse(self, head: ListNode) -> ListNode:
        if not head:
          return None
          
        newHead = head   # head diye suru always 
         if head.next:
           newHead= self.reverse (head.next)
           head.next.next = head
         head.next = None
      return newHead
