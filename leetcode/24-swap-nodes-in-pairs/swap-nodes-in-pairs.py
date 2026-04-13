# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapi(self, item):
        if item is None or item.next is None:
            return
        value = item.val
        item.val = item.next.val
        item.next.val = value
        if item.next.next is None:
            return
        self.swapi(item.next.next)

    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        self.swapi(temp)
        return head
        