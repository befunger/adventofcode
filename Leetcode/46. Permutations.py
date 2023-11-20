import copy
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Recursive algo.
        return self.rec([], nums)

    def rec(self, prefix: List[int], nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [prefix + nums]
        output = []
        for perm in [prefix + [num] for num in nums]:
            new_nums = copy.copy(nums)
            new_nums.remove(perm[-1])
            output.extend(self.rec(perm, new_nums))
        return output