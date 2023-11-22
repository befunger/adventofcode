class Solution:
    def numTrees(self, n: int) -> int:
        # We can any digit k at the root.
        # We must then put nodes [1, k-1] on its left and [k+1, n] on its right
        # If there are l ways to arrange left side and r to arrange right side that gives us l*r possible arrangings
        # We can calculate l by figuring out numTrees(k-1) and r from numTrees(n-k)
        # Note: We will probably recalculate a lot of numTrees() with same value, so we should cache results
        
        cached_nums = {} # Hashmap for duplicate calculations
        return self.rec(n, cached_nums)

    def rec(self, n: int, cached_nums: dict):
        if n <= 1: # Base cases for 0 and 1
            return 1
        if n in cached_nums: # Use cached value (catches base cases)
            return cached_nums[n]

        num_trees = 0
        for k in range(1, n+1):
            # Get left result
            l = self.rec(k-1, cached_nums)
            cached_nums[k-1] = l
            # Get right result
            r = self.rec(n-k, cached_nums)
            cached_nums[n-k] = r
            # Combine
            num_trees += l*r
            cached_nums[n] = num_trees
        return num_trees
