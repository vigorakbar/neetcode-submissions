# Sorting
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False

# Time: O(nlogn) for sorting the nums
# Space: O(1) or O(n) depending on the sorting algorithm
