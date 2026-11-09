# Using fixed counter hash table
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        resultDict = defaultdict(list)

        for text in strs:
            counter = [0] * 26
            for char in text:
                counter[ord(char) - ord('a')] += 1
            resultDict[tuple(counter)].append(text)

        return list(resultDict.values())

# Time: O(m * n) for iterating each word. m number of string, n longest string characters count
# Space:
# - O(m) auxilary space only. each word m need only one record
# - O(m * n) if output list is counted


# # sorting approach
# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         result = defaultdict(list)

#         for text in strs:
#             sortedTxt = "".join(sorted(text))
#             result[sortedTxt].append(text)
        
#         return list(result.values())

# # Time: O(m * nlogn) for sorting each word
# # Space: O(m * n) for storing dict with full word key