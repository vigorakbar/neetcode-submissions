# Reverse and merge approach

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        prev = slow.next = None

        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        
        first = head
        second = prev
        while second:
            tmp1 = first.next
            tmp2 = second.next

            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2

# Time: O(n)
# Space: O(1)


# # Recursive approach

# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next

# class Solution:
#     def reorderList(self, head: Optional[ListNode]) -> None:
#         def recursive(root: ListNode, cur: ListNode) -> ListNode:
#             if not curr:
#                 return root

#             root = recursive(root, cur.next)
#             if not root:
#                 return None
            
#             tmp = None
#             if root == cur or root.next == cur:
#                 curr.next = None
#             else:
#                 tmp = root.next
#                 root.next = cur
#                 cur.next = tmp
            
#             return tmp

#         head = recursive(head, head.next)

# # stack approach

# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next

# class Solution:
#     def reorderList(self, head: Optional[ListNode]) -> None:
#         if not head: return None

#         stack = []
#         current = head
#         while current:
#             stack.append(current)
#             current = current.next
#         stackLen = len(stack)

#         current = head
#         for i in range((stackLen - 1) // 2):
            
#             temp = current.next
#             popped = stack.pop()
#             current.next = popped
#             popped.next = temp
#             current = temp

#         if stackLen % 2 == 1:
#             current.next = None
#         else:
#             current.next.next = None

# # Time: O(n)
# # Space: O(n)