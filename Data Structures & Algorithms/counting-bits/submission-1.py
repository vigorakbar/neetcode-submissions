# DP approach (Optimal)

class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n+1)
        for i in range(n+1):
            res[i] = res[i >> 1] + (i & 1)

        return res

# Time: O(n)
# Space: O(1) extra space

# # DP approach

# class Solution:
#     def countBits(self, n: int) -> List[int]:
#         res = [0] * (n + 1)
#         offset = 1

#         for i in range(1, n + 1):
#             if offset * 2 == i:
#                 offset = i
#             res[i] = 1 + res[i - offset]

#         return res

# # Time: O(n)
# # Space: O(1) extra space

# # Bit manipulation approach

# class Solution:
#     def countBits(self, n: int) -> List[int]:
#         res = []
#         for i in range(n + 1):
#             count = 0
#             while i:
#                 i &= i - 1
#                 count += 1
#             res.append(count)
#         return res

# # Time: O(nlogn)
# # Space: O(1) extra space
