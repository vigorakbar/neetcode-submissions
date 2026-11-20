# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head: return None

        total = 0
        current = head
        while current:
            total += 1
            current = current.next
        
        position = 1
        current = head
        prev = None
        while position < (total - n + 1):
            temp = current
            current = current.next
            prev = temp
            position += 1
        
        if prev:
            prev.next = current.next
            current.next = None
        else:
            return head.next
        
        return head

# Time: O(n)
# Space: O(1)


