# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        root = ListNode(0)
        temp = root
        
        while l1 or l2 or carry:
            sum_val = 0

            if l1:
                sum_val += l1.val
                l1 = l1.next

            if l2:
                sum_val += l2.val
                l2 = l2.next
                
            sum_val += carry

            temp.next = ListNode(sum_val % 10)
            temp = temp.next

            carry = sum_val // 10
            
        return root.next





