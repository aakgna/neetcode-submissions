class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        track = dict()
        for n in nums:
            if n in track:
                track[n] += 1
            else:
                track[n] = 1
            sorted_dict = {k: v for k, v in sorted(track.items(), key=lambda item: item[1], reverse=True)}
        res = list(sorted_dict.keys())
        return res[:k]