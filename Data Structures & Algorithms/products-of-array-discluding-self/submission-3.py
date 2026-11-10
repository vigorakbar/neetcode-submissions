# Prefix suffix with no extra array approach
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        # prefix
        for i in range(1, len(nums)):
            result[i] = result[i - 1] * nums[i - 1]
        # suffix
        suffix = 1
        for i in range(len(nums) - 2, -1, -1):
            suffix *= nums[i + 1]
            result[i] = result[i] * suffix
        
        return result

# Without division operation
# Time: O(n) for iterating nums
# Space:
# - Extra space: O(1)
# - Output array: O(n)


# # Prefix Suffix with extra arrays approach
# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         # store 2 list, 1 to store where in index i it will be all product in the left side, and the other all product in the right side, the result will be multiplication of both list in the same index
#         left = [1] * len(nums)
#         right = [1] * len(nums)
#         result = []
        
#         # populate left
#         for i in range(1, len(nums)):
#             left[i] = left[i - 1] * nums[i - 1]
#         # populate right
#         for i in range(len(nums) - 2, -1, -1):
#             right[i] = right[i + 1] * nums[i + 1]
        
#         for i in range(len(nums)):
#             result.append(left[i] * right[i])
        
#         return result

# # Time: O(n) for iterating nums
# # Space: O(n) for storing left, right the length of nums

# # Division approach
# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         # if there's 2 or more zero, all will be zero
#         # if there's 1 zero, all zero except one element
#         # else normal operation
#         product = 1
#         zeroCount = 0
#         for num in nums:
#             if num:
#                 product *= num
#             else:
#                 zeroCount += 1
        
#         if zeroCount > 1:
#             return [0] * len(nums)
        
#         if zeroCount:
#             return [0 if num else product for num in nums]
#         else:
#             return [product // num for num in nums]
# # Time: O(n)
# # Space:
# # - Extra: O(1)
# # - Output: O(n)
