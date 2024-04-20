class Solution:
    def reorderList(self, head: ListNode) -> None:
        if head == None or head.next == None: return
     ######  find middle  f=2s
        slow, fast = head, head.next 
        while fast != None and fast.next != None:
            slow = slow.next   # 1 ghor 
            fast = fast.next.next  # 2 ghor upore
        
        prev, curr = None, slow       ##### reverse second half,   last slow pointer ke curr,   prev=None lekha mane separate 1>2>3>4...  1>2>None 
        while curr != None:
            tmp = curr.next                # tmp= 3
            curr.next = prev               # 
            prev = curr
            curr = tmp
        
        n1, n2 = head, prev
        while n2.next != None:
            tmp1 = n1.next,             tmp2 = n2.next
            n1.next = n2            
            n2.next = n1            
            n1 = tmp1
            n2 = tmp2



            
