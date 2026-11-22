# Recursion DFS approach

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p and not q: return False
        if q and not p: return False

        if not p and not q: return True

        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

# Time: O(n)
# Space: O(n)


# # Iteration DFS approach

# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right

# class Solution:
#     def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
#         if not p and not q: return True

#         stack = [[p, q]]

#         while len(stack):
#             p, q = stack.pop()
#             if p and q:
#                 if p.val != q.val:
#                     return False
#                 stack.append([p.left, q.left])
#                 stack.append([p.right, q.right])
#             elif not p and not q:
#                 continue
#             else:
#                 return False
#         return True

# # Time: O(n)
# # Space: O(n)


# # BFS approach

# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right

# class Solution:
#     def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
#         queue = deque([[p, q]])
#         while len(queue):
#             p, q = queue.popleft()
#             if p and q:
#                 if p.val != q.val:
#                     return False
#                 queue.append([p.left, q.left])
#                 queue.append([p.right, q.right])
#             elif not p and not q:
#                 continue
#             else:
#                 return False

#         return True

# # Time: O(n)
# # Space: O(n)