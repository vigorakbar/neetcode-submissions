class Solution:
    def findMin(self, nums: List[int]) -> int:
        # check first and last element to see if the array is rotated
        #   - if i < j it's not rotated (i is the answer)
        #   - if j > i it's rotated. so need to find the smallest answer
        #     - find mid = length // 2
        #     - if nums[mid] is > nums[i], go right. i = mid + 1
        #     - else if nums[mid] is < nums[i], go left. j = mid

        i = 0
        j = len(nums) - 1

        while i < j:
            if nums[i] < nums[j]: return nums[i]
            mid = ((j - i) // 2) + i
            # print(i, j, mid)
            if nums[mid] > nums[i]:
                i = mid + 1
            elif nums[mid] < nums[i]:
                j = mid
            else:
                if nums[i] < nums[j]:
                    j = i
                else:
                    i = j
        # print(i, j, mid)
        
        return nums[i]