# Fast and slow pointers

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        first = second = head

        while second and second.next:
            first = first.next
            second = second.next.next
            if first == second:
                return True
        
        return False

# Time: O(n)
# Space: O(1)

# # Naive using set

# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next

# class Solution:
#     def hasCycle(self, head: Optional[ListNode]) -> bool:
#         visited = set()
#         current = head
#         while current:
#             if current in visited: return True
#             visited.add(current)
#             current = current.next

#         return False
            
# # Time: O(n)
# # Space: O(n)
