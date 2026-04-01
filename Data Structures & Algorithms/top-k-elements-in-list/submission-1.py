class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for x in nums:
            if x in freq:
                freq[x] += 1
            else:
                freq[x] = 1
        buckets = [[] for _ in range(len(nums) + 1)]
        for key, value in freq.items():
            buckets[value].append(key)

        result = []
        for i in range(len(buckets) - 1, 0, -1):
            if len(result) < k:
                for x in buckets[i]:
                    result.append(x)
            else:
                return result
        return result