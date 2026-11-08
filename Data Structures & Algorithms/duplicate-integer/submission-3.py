# Using set length comparison
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums)

# Time: O(n) because set(nums) iterating through the list
# Space: O(n) because creating new set
# Always process the whole list (compared to early return version)