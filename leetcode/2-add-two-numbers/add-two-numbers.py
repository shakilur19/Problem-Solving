# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        carry = 0
        ans = ListNode(0)
        head = ans
        while (l1 or l2 or carry):
            dig1 = l1.val if l1 else 0
            dig2 = l2.val if l2 else 0
            
            sum = dig1 + dig2 + carry
            digit = sum % 10
            carry = sum // 10

            node = ListNode(digit)
            head.next = node
            head = head.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return ans.next
        