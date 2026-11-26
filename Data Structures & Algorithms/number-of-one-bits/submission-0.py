# Bit mask approach - optimal
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            n &= n - 1
            res += 1
        return res

# # Time: O(1)
# # Space: O(1)

# # Native approach
# class Solution:
#     def hammingWeight(self, n: int) -> int:
#         return bin(n).count('1')

# # Time: O(1)
# # Space: O(1)

# # Bit Mask approach - 1
# class Solution:
#     def hammingWeight(self, n: int) -> int:
#         res = 0
#         for i in range(32):
#             if (1 << i) & n:
#                 res += 1
#         return res

# # Time: O(1)
# # Space: O(1)

# # Bit Mask approach - 2
# class Solution:
#     def hammingWeight(self, n: int) -> int:
#         res = 0
#         while n:
#             res += 1 if n & 1 else 0
#             n = n >> 1
#         return res

# # Time: O(1)
# # Space: O(1)
