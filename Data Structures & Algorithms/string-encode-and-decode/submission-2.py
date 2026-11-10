# Encode per word
class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedList = []
        for text in strs:
            encodedList.extend([str(len(text)), "#", text])
        return "".join(encodedList)

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        
        while(i < len(s)):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            decoded.append(s[i:j])
            i = j
        return decoded

# Time: O(m + n) iterating m total length of all strings and n total string
# Space: O(m + n) storing m and n

# # Encode with header once
# class Solution:

#     def encode(self, strs: List[str]) -> str:
#         if not strs:
#             return ""

#         lengthList = []
#         for text in strs:
#             lengthList.append(str(len(text)))
#         return ",".join(lengthList) + ",#" + "".join(strs)

#     def decode(self, s: str) -> List[str]:
#         print(s)
#         if not s:
#             return []

#         lengthList = []
#         i = 0
#         while s[i] != "#":
#             j = i
#             while (s[j] != ","):
#                 j += 1
#             lengthList.append(int(s[i:j]))
#             i = j + 1
        
#         i += 1
#         result = []
#         for length in lengthList:
#             result.append(s[i:i + length])
#             i += length
#         return result
