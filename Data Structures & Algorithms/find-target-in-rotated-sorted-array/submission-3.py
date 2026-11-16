class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        mid = (l + r) // 2
        while l < r:
            mid = (l + r) // 2
            print(l, r, mid)
            if target == nums[mid]: return mid
            if nums[l] < nums[r]:
                if target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                # 3,4,5,6,7,1,2
                if nums[mid] > nums[r]:
                    if target > nums[mid]:
                        l = mid + 1
                    else:
                        if target > nums[l]:
                            r = mid - 1
                        elif target < nums[l]:
                            l = mid + 1
                        else:
                            return l
                # 6, 7, 1, 2, 3, 4, 5
                else:
                    if target < nums[mid]:
                        r = mid - 1
                    else:
                        if target < nums[l]:
                            l = mid + 1
                        elif target > nums[l]:
                            r = mid - 1
                        else:
                            return l
        print (l, r, mid)
        return l if nums[l] == target else -1


            