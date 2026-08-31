import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        arr = []
        res = -1
        for n in nums:
            heapq.heappush(arr, -n)
        for i in range(k):
            res = heapq.heappop(arr)
        return -res