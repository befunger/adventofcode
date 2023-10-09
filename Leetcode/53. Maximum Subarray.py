class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        n = len(nums)

        max_ending_here = nums[0]
        max_sum = nums[0]
        # Iterate through array from start to end: Outer loop O(n)
        for i in range(1, n):
            if max_ending_here >= 0: # If previous gives positive impact, keep and add current
                max_ending_here += nums[i]
            else: # Else if previous give negative impact, discard and only include current
                max_ending_here = nums[i]

            if max_ending_here > max_sum: # Update best if we find new max
                max_sum = max_ending_here

        return max_sum