# DFS approach

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rec(self, node, minVal, maxVal):
        if not node: return True
        if not (minVal < node.val < maxVal): return False
        # everytime going left, need to be less than the ancestors
        # everytime going right, need to be greater than the acnestors
        return self.rec(node.left, minVal, node.val) and self.rec(node.right, node.val, maxVal)
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.rec(root, -math.inf, math.inf)

# Time: O(n)
# Space: O(n)

# # BFS approach

# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right

# class Solution:
#     def isValidBST(self, root: Optional[TreeNode]) -> bool:
#         if not root: return True
#         queue = deque([[root, -math.inf, math.inf]])
#         while queue:
#             node, minVal, maxVal = queue.popleft()
#             if not (minVal < node.val < maxVal):
#                 return False
#             if node.left:
#                 queue.append([node.left, minVal, node.val])
#             if node.right:
#                 queue.append([node.right, node.val, maxVal])
#         return True

# # Time: O(n)
# # Space: O(n)