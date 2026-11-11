class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1

        while i < j:
            if not s[i].isalnum():
                i += 1
            elif not s[j].isalnum():
                j -= 1
            else:
                if s[i].lower() != s[j].lower():
                    return False
                i += 1
                j -= 1

        return True

# Time: O(n) for iterating string
# Space: O(1) no extra space

# # Using regex cleanup
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         palStr = re.findall(r'[a-zA-Z0-9]', s)
#         palStr = "".join(palStr).lower()

#         i = 0
#         j = len(palStr) - 1
#         valid = True

#         while i < j:
#             if palStr[i] != palStr[j]:
#                 valid = False
#                 return valid
#             i += 1
#             j -= 1

#         return valid

# # Time: O(n)
# # Space: O(n) for storing cleaned up string