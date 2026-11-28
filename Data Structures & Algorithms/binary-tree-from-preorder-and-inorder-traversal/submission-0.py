# Morris Traversal approach

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        head = TreeNode(None)
        curr = head
        i, j, n = 0, 0, len(preorder)
        while i < n and j < n:
            # Go right and then as far left as possible
            curr.right = TreeNode(preorder[i], right = curr.right)
            curr = curr.right
            i += 1
            while i < n and curr.val != inorder[j]:
                curr.left = TreeNode(preorder[i], right = curr)
                curr = curr.left
                i += 1
            j += 1
            while curr.right and j < n and curr.right.val == inorder[j]:
                prev = curr.right
                curr.right = None
                curr = prev
                j += 1
        
        return head.right

# Time: O(n)
# Space: O(1) extra space

# # DFS Optimal

# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right

# class Solution:
#     def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
#         preIdx = inIdx = 0

#         def dfs(limit):
#             nonlocal preIdx, inIdx

#             if preIdx >= len(preorder):
#                 return None
#             if limit == inorder[inIdx]:
#                 inIdx += 1
#                 return None
            
#             root = TreeNode(preorder[preIdx])
#             preIdx += 1
#             root.left = dfs(root.val)
#             root.right = dfs(limit)
#             return root

#         return dfs(math.inf)
        
# # Time: O(n)
# # Space: O(n)

# # Hash Map + DFS

# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right

# class Solution:
#     def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
#         indices = {val: idx for idx, val in enumerate(inorder)}

#         self.preIdx = 0
#         def dfs(l,r):
#             if l > r:
#                 return None
#             rootVal = preorder[self.preIdx]
#             self.preIdx += 1
#             root = TreeNode(rootVal)
#             mid = indices[rootVal]
#             root.left = dfs(l, mid - 1)
#             root.right = dfs(mid + 1, r)
#             return root
        
#         return dfs(0, len(inorder) - 1)

# # Time: O(n)
# # Space: O(n)

# # DFS Recursive - basic

# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right

# class Solution:
#     def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
#         if not preorder or not inorder:
#             return None
        
#         root = TreeNode(preorder[0])
#         mid = inorder.index(preorder[0])

#         root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
#         root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

#         return root

# # Time: O(n^2)
# # Space: O(n^2)
