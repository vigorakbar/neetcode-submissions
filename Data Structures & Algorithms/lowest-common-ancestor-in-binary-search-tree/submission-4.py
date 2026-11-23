# Iteration approach

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curr = root

        while curr:
            if p.val < curr.val and q.val < curr.val:
                curr = curr.left
            elif p.val > curr.val and q.val > curr.val:
                curr = curr.right
            else:
                return curr
        
        return curr


        
# Time: O(h) h is max height of the tree
# Space: O(1)

# # recursion approach

# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right

# class Solution:
#     def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
#         if not root or not p or not q: return None
#         if (min(p.val, q.val) > root.val):
#             return self.lowestCommonAncestor(root.right, p, q)
#         if (max(p.val, q.val) < root.val):
#             return self.lowestCommonAncestor(root.left, p, q)
#         return root

# # Time: O(h)
# # Space: O(h)