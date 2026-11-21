# Divide and Conquer approach

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        return self.divide(lists, 0, len(lists) - 1)
    
    def divide(self, lists, l, r):
        if l > r:
            return None
        if l == r:
            return lists[l]
        
        mid = (l + r ) // 2
        left = self.divide(lists, l, mid)
        right = self.divide(lists, mid + 1, r)

        return self.conquer(left, right)
    
    def conquer(self, l1, l2):
        dummy = ListNode(0)
        curr = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        if l1: curr.next = l1
        else: curr.next = l2

        return dummy.next

# Time: O(nlogk)
# Space: O(logk)

# # min-heap (priority queue) approach

# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next

# class NodeWrapper:
#     def __init__(self, node):
#         self.node = node
    
#     def __lt__(self, other):
#         return self.node.val < other.node.val

# class Solution:    
#     def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
#         if len(lists) == 0:
#             return None
        
#         res = ListNode(0)
#         curr = res
#         minHeap = []

#         for node in lists:
#             if node is not None:
#                 heapq.heappush(minHeap, NodeWrapper(node))

#         while minHeap:
#             node_wrapper = heapq.heappop(minHeap)
#             curr.next = node_wrapper.node
#             curr = curr.next

#             if node_wrapper.node.next:
#                 heapq.heappush(minHeap, NodeWrapper(node_wrapper.node.next))
        
#         return res.next