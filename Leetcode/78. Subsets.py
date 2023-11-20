class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Start with ans = [[]], for each num in list, add duplicates of all entries with the num added.
        ans = [[]]
        for num in nums:
            ans += [s + [num] for s in ans]
        return ans
