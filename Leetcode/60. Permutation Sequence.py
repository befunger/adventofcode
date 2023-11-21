import math
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [str(x+1) for x in range(n)] # ['1', '2', ..., 'n']
        N = math.factorial(n-1)
        return self.rec(N, k-1, nums) # k-1 because algorithm is based on 0-indexing

    def rec(self, N, k, nums):
        if len(nums) == 1: return nums[0]
        div, res = k//N, k%N
        char = nums[div]
        del nums[div]
        return char + self.rec(N//len(nums), res, nums)