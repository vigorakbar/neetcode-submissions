# BFS approach

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []

        queue = deque([root])
        res = []
        while queue:
            currNodes = []
            for _ in range(len(queue)):
                node = queue.popleft()
                currNodes.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            res.append(currNodes)

        return res
            
# Time: O(n)
# Space: O(n)


# # Recursive approach DFS

# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right

# class Solution:
#     def recursion(self, root, level, res):
#         if not root: return res
#         if len(res) < level:
#             res.append([root.val])
#         else:
#             res[level - 1].append(root.val)
#         self.recursion(root.left, level + 1, res)
#         self.recursion(root.right, level + 1, res)
#         return res

#     def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
#         return self.recursion(root, 1, [])

# # Time: O(n)
# # Space: O(n)
