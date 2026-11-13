# (Optimal) Sliding window approach using hash map

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        result = 0
        visited = {}

        for r in range(len(s)):
            if s[r] in visited:
                l = max(l, visited[s[r]] + 1)
            visited[s[r]] = r
            result = max(result, r - l + 1)
        
        return result

# Time: O(n) iterating length of string s
# Space: O(m) storing m unique visited characters
# No not to delete map. map become last seen index instead of updated records of current window members

# # Sliding window using hash set
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         charSet = set()
#         l = 0
#         result = 0

#         for r in range(len(s)):
#             while s[r] in charSet:
#                 charSet.remove(s[l])
#                 l += 1
#             charSet.add(s[r])
#             result = max(result, r - l + 1)
#         return result

# # Time: O(n) n is length of s
# # Space: O(m) m unique char set

# # Sliding window approach using hash map
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         if not s: return 0
#         if len(s) == 1: return 1

#         l = 0
#         r = 1
#         maxLen = 1
#         visited = {}
#         while r < len(s):
#             visited[s[l]] = l
#             if s[r] in visited:
#                 prevVisited = visited[s[r]]
#                 visited[s[r]] = r
#                 while l < prevVisited + 1:
#                     del visited[s[l]]
#                     l += 1
#                 if r <= l:
#                     r = l + 1
#             else:
#                 visited[s[r]] = r
#                 maxLen = max(maxLen, r - l + 1)
#                 r += 1

#         return maxLen

# # O(n) 
# # O(m)
# # Complicated and unoptimal
