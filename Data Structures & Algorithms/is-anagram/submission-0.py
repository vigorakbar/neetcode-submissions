# Because we have a fixed 26 character (assuming lowercase a-z),
# we can skip hashing and use array instead
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        counter = [0] * 26
        for i in range(len(s)):
            counter[ord(s[i]) - ord('a')] += 1
            counter[ord(t[i]) - ord('a')] -= 1
        
        for count in counter:
            if count != 0:
                return False

        return True

# Time: O(n) for iterating throught the string
# Space: O(1) for using fixed 26 length array

# # Hash map
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if (len(s) != len(t)):
#             return False

#         countMap = {}
#         for i in range(len(s)):
#             countMap[s[i]] = countMap.get(s[i], 0) + 1
#             countMap[t[i]] = countMap.get(t[i], 0) - 1
#         for val in countMap.values():
#             if (val != 0):
#                 return False
#         return True

# # Time: O(n) for iterating through the string. need hashing
# # Space: O(1) max 26 character only

# # Sort approach
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False

#         return sorted(s) == sorted(t)

# # Time: O(nlogn) for sorting
# # Space: O(n) for storing the sorted list     
   