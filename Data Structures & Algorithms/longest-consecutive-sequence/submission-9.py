# Hash Map approach
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # store in Map, where the value is how many consecutives value
        # only need to see the "edges" of consecutive numbers
        
        numDict = defaultdict(int)
        longest = 0
        for num in nums:
            if not numDict[num]:
                numDict[num] = numDict[num - 1] + numDict[num + 1] + 1
                numDict[num - numDict[num - 1]] = numDict[num]
                numDict[num +  numDict[num + 1]] = numDict[num]
                longest = max(longest, numDict[num])
        
        return longest

# Time: O(n) for iterating nums
# Space: O(n) for sotring defaultdict nums

# # Set approach
# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         numSet = set(nums)
#         longest = 0

#         for num in numSet:
#             if (num - 1) not in numSet:
#                 count = 1
#                 while (num + count) in numSet:
#                     count += 1
#                 if count > longest: longest = count
#         return longest

# # Time: O(n) for iterating numSet, worst case in while loop is just 2n
# # Space: O(n) for storing numSet

# # Sorting approach
# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         if not nums:
#             return 0

#         sortedNums = sorted(nums)
        
#         current = 1
#         longest = 1
#         for i in range(len(sortedNums) - 1):
#             if sortedNums[i + 1] - sortedNums[i] == 1:
#                 current += 1
#                 if (current > longest): longest = current
#             elif sortedNums[i + 1] - sortedNums[i] == 0:
#                 continue 
#             else:
#                 current = 1
#         return longest

# # Time: O(nlogn) for sorting
# # Space: O(n) for storing sortedNums
