# Morris Traversal approach

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        curr = root
        while curr:
            if not curr.left:
                k -= 1
                if k == 0:
                    return curr.val
                curr = curr.right
            else:
                pred = curr.left
                while pred.right and pred.right != curr:
                    pred = pred.right
                if not pred.right:
                    pred.right = curr
                    curr = curr.left
                else:
                    pred.right = None
                    k -= 1
                    if k == 0:
                        return curr.val
                    curr = curr.right
        return -1

# Time: O(n)
# Space: O(1)

# # DFS recursive

# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right

# class Solution:
#     def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
#         count = k
#         res = root.val

#         def dfs(root):
#             nonlocal count, res

#             if not root:
#                 return
            
#             dfs(root.left)
#             if count == 0:
#                 return
#             count -= 1
#             if count == 0:
#                 res = root.val
#                 return
#             dfs(root.right)
        
#         dfs(root)

#         return res

# # Time: O(n)
# # Space: O(n)

# # DFS Iterative

# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right

# class Solution:
#     def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
#         stack = []
#         curr = root

#         while stack or curr:
#             while curr:
#                 stack.append(curr)
#                 curr = curr.left
#             curr = stack.pop()
#             k -= 1
#             if k == 0:
#                 return curr.val
#             curr = curr.right

# # Time: O(n)
# # Space: O(n)