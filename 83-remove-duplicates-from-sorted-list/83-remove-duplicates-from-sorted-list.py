# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        while(curr!=None):
            uniq = curr
            curr = curr.next
            while(curr != None and curr.val==uniq.val):
                curr = curr.next
            if(curr!=None):
                uniq.next = curr
            else:
                uniq.next = None
        return head
            
        