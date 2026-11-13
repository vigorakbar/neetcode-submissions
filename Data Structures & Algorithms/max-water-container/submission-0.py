# Two Pointer approach
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        l = 0
        r = len(heights) - 1
        while l < r:
            area = (r - l) * min(heights[l], heights[r])
            res = max(res, area)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return res

# Time: O(n) iterating two pointers n time
# Space: O(1)

# # Brute Force Approach
# class Solution:
#     def maxArea(self, heights: List[int]) -> int:
#         res = 0
#         for i in range(len(heights) - 1):
#             for j in range(i + 1, len(heights)):
#                 res = max(res, (j - i) * min(heights[i], heights[j]))

#         return res

# # Time: O(n^2) for iterating i j
# # Space: O(1)