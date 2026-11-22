# Recursive DFS approach

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

# Time: O(n)
# Space: O(n)

# # Iterative DFS approach

# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right

# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         if not root: return 0
#         stack = [[root, 1]]
#         n = 0
#         while len(stack):
#             node, level = stack.pop()
#             n = max(n, level)
            
#             if node.left: stack.append([node.left, level + 1])
#             if node.right: stack.append([node.right, level + 1])

#         return n

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
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         if not root: return 0
#         queue = deque([[root, 1]])
#         n = 0
#         while len(queue):
#             node, level = queue.popleft()
#             if level > n: n = level
#             if node.left: queue.append([node.left, level + 1])
#             if node.right: queue.append([node.right, level + 1])
        
#         return n

# # Time: O(n)
# # Space: O(n)
