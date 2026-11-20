# Two pointer

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head
        while n > 0:
            right = right.next
            n -= 1

        while right:
            left = left.next
            right = right.next

        left.next = left.next.next
        
        return dummy.next

# Time: O(n)
# Space: O(1)

# # Two Pass Iteration approach

# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next

# class Solution:
#     def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
#         if not head: return None

#         total = 0
#         current = head
#         while current:
#             total += 1
#             current = current.next
        
#         position = 1
#         current = head
#         prev = None
#         while position < (total - n + 1):
#             temp = current
#             current = current.next
#             prev = temp
#             position += 1
        
#         if prev:
#             prev.next = current.next
#             current.next = None
#         else:
#             return head.next
        
#         return head

# # Time: O(n)
# # Space: O(1)


# # Recursion approach

# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next

# class Solution:
#     def recursion(self, head, n):
#         if not head: return None

#         head.next = self.recursion(head.next, n)
#         n[0] -= 1
#         if n[0] == 0:
#             return head.next
        
#         return head

#     def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
#         return self.rec(head, [n])
        
# # Time: O(n)
# # Space: O(n)