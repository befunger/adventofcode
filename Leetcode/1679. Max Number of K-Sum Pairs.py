class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # Find number of "pairs" that sum to k (no reusing)
        counts = defaultdict(int)
        pairs = 0
        for x in nums:
            if counts[k-x] > 0:
                pairs += 1
                counts[k-x] -= 1
            else:
                counts[x] += 1
        return pairs
