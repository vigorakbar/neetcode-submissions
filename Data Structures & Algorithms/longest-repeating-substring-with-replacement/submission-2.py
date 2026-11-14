# Optimal Sliding Window approach
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        maxSoFar = 0
        res = 0
        l = 0

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            maxSoFar = max(maxSoFar, count[s[r]])

            while (r - l + 1) - maxSoFar > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)

        return res

# Time: O(n)
# Space: O(m)

# # Sliding window
# class Solution:
#     def characterReplacement(self, s: str, k: int) -> int:
#         charSet = set(s)
#         res = 0

#         for char in charSet:
#             l = 0
#             count = 0
#             for r in range(len(s)):
#                 if s[r] == char:
#                     count += 1
                
#                 while (r - l + 1) - count > k:
#                     if s[l] == char:
#                         count -= 1
#                     l += 1

#                 res = max(res, r - l + 1)
#         return res

# # Time: O(n * m) n string length, m unique string
# # Space: O(m)