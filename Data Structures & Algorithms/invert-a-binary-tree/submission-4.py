# BFS approach

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return None
        queue = deque([root])
        while len(queue):
            node = queue.popleft()
            node.left, node.right = node.right, node.left

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return root

# Time: O(n)
# Space: O(n)

# # DFS Iterative approach

# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right

# class Solution:
#     def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
#         if not root: return None
#         stack = [root]
#         while len(stack):
#             node = stack.pop()
#             temp = node.left
#             node.left = node.right
#             node.right = temp

#             if node.left:
#                 stack.append(node.left)
#             if node.right:
#                 stack.append(node.right)
#         return root
            
# # Time: O(n)
# # Space: O(n)


# # DFS Recursive approach

# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right

# class Solution:
#     def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
#         if not root: return None

#         self.invertTree(root.left)
#         self.invertTree(root.right)

#         temp = root.left
#         root.left = root.right
#         root.right = temp

#         return root

# # Time: O(n)
# # Space: O(n)