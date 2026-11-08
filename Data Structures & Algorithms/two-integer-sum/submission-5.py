# One Pass Hash Map
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numIndices = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in numIndices:
                return [numIndices[diff], i]
            numIndices[num] = i

# Time: O(n) for iterating nums
# Space: O(n) for storing hash

# # Two Pass Hash Map
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         numIndices = {}

#         for i, num in enumerate(nums):
#             numIndices[num] = i
        
#         for i, num in enumerate(nums):
#             diff = target - num
#             if diff in numIndices and numIndices[diff] != i:
#                 return [i, numIndices[diff]]
#         return []

# # Time: O(n) for iterating nums
# # Space: O(n) for storing hash

# # Sorted
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         numsWithIdx = []
        
#         for i, num in enumerate(nums):
#             numsWithIdx.append([num, i])

#         numsWithIdx.sort()
#         i = 0
#         j = len(numsWithIdx) - 1

#         while i < j:
#             if numsWithIdx[i][0] + numsWithIdx[j][0] == target:

#                 return sorted([numsWithIdx[i][1], numsWithIdx[j][1]])
#             if numsWithIdx[i][0] + numsWithIdx[j][0] > target:
#                 j -= 1
#             else:
#                 i += 1

# # Time: O(nlogn) for sorting
# # Space: O(n) for sorting


# # Brute force
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#        for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]

# # Time: O(n^2)
# # Space: O(1)