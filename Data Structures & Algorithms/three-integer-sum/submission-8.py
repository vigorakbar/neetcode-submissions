# Two pointers approach
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        result = []
        for i in range(len(nums)):
            if nums[i] > 0:
                break;
            if i > 0 and nums[i] == nums[i-1]:
                continue;

            left = i + 1
            right = len(nums) - 1

            while left < right:
                current = nums[i] + nums[left] + nums[right]
                if current > 0:
                    right -= 1
                elif current < 0:
                    left += 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left - 1] and left < right:
                        left +=1
                
        
        return result

# Time: O(n^2)
# Space: O(1) excluding output array

# # Hash map approach
# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         nums.sort()
#         count = defaultdict(int)

#         result = []

#         for num in nums:
#             count[num] += 1
        
#         for i in range(len(nums)):
#             count[nums[i]] -= 1
#             if i and nums[i] == nums[i-1]:
#                 continue
#             for j in range(i+1, len(nums)):
#                 count[nums[j]] -= 1
#                 if j - 1 > i and nums[j] == nums[j - 1]:
#                     continue
#                 target = -(nums[i] + nums[j])
#                 if count[target] > 0:
#                     result.append([nums[i], nums[j], target])
#             for j in range(i+1, len(nums)):
#                 count[nums[j]] += 1

#         return result
        
# # Time: O(n^2)
# # Space: O(n) for frequency map
# # - plus m of unique triplets if counting output space

# # Brute force
# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         result = set()
#         nums.sort()
#         for i in range(len(nums) - 2):
#             for j in range(i + 1, len(nums) - 1):
#                 for k in range(j + 1, len(nums)):
#                     if nums[i] + nums[j] + nums[k] == 0:
#                         result.add(
#                             (nums[i], nums[j], nums[k])
#                         )
#         return [list(x) for x in result]

# # Time: O(n^3)
# # Space: O(m) m is unique triplet in a stored set