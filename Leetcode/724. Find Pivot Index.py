class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # Cumulative sum approach
        cum_sum = [0]
        for num in nums:
            cum_sum.append(cum_sum[-1] + num)
        cum_sum.append(cum_sum[-1])

        for i,_ in enumerate(nums,start=1):
            if cum_sum[i-1] == cum_sum[-1] - cum_sum[i]:
                # Decrement by 1 because of 1-indexing
                return i-1

        # No pivot found
        return -1
