# Using set
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

# Time: O(n) for iterating through the list
# Space: O(n) for storing the set
# can return early when duplicate found early