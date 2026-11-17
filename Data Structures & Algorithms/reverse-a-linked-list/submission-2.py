# Iteration using prev node
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head
        #       0,   1, 2, 3
        # prev current
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp

        return prev

# Time: O(n)
# Space: O(1)

# # Recursion approach
# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next

# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if not head: return None
#         newHead = head
#         if head.next:
#             newHead = self.reverseList(head.next)
#             head.next.next = head
#         head.next = None

#         return newHead
        

# # Iteration using next Node
# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next

# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if not head or not head.next: return head

#         current = head
#         nextNode = current.next
#         temp = nextNode.next
#         nextNode.next = current
#         current.next = None
#         current = nextNode
#         nextNode = temp

#         while nextNode:
#             temp = nextNode.next
#             nextNode.next = current
#             current = nextNode
#             nextNode = temp
            
#         return current
        