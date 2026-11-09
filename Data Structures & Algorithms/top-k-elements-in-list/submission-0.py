# Bucket Sort approach
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for x in range(len(nums)+1)]

        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        for num, count in count.items():
            buckets[count].append(num)

        result = []
        for i in range(len(nums), 0, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result

# Time: O(n)
# Space: O(n)

# # Min-Heap approach
# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         numCount = {}
#         for num in nums:
#             numCount[num] = numCount.get(num, 0) + 1
        
#         minHeap = []
#         for num, count in numCount.items():
#             heapq.heappush(minHeap, (count, num))
#             if (len(minHeap) > k):
#                 heapq.heappop(minHeap)
        
#         return [num for count, num in minHeap]

# # Time: O(nlogk) for iterating n and push/pop heap k
# # Space: O(n + k) for storing numCount and heap k

# # Sorting approach
# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         counter = {}
#         for num in nums:
#             counter[num] = counter.get(num, 0) + 1
#         sortedKeys = sorted(counter, key=counter.get, reverse=True)
#         return sortedKeys[:k]

# # Time: O(nlogn) for sorting counter
# # Space: O(n) for storing counter