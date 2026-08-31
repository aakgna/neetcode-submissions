import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        nums = sorted(nums)
        nums.reverse()
        self.top_k = list()
        for n in nums[0:k]:
            heapq.heappush(self.top_k, n)

    def add(self, val: int) -> int:
        if len(self.top_k) > 0 and val <= self.top_k[0]:
            v = heapq.heappop(self.top_k)
            heapq.heappush(self.top_k, v)
            return v
        if len(self.top_k) > 0 and len(self.top_k) == self.k:
            v = heapq.heappop(self.top_k)
        heapq.heappush(self.top_k, val)
        v = heapq.heappop(self.top_k)
        heapq.heappush(self.top_k, v)
        return v