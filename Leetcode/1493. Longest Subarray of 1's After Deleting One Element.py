class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # Return 0 if no subarray with 1s after deleting one element
        if not 1 in nums or len(nums) == 1:
            return 0

        # If all 1s, one must be deleted still
        if not 0 in nums: 
            return len(nums)-1

        # Iterate from start counting 1s, allow hitting one 0 (we can delete)
        # Once second 0 hit, remove the number of 1s from prior to first zero
        # At each step, check if count higher than max

        groups = []
        # Get array of each group of 1s
        count = 0
        for num in nums:
            count += num
            if not num:
                groups.append(count)
                count = 0
        groups.append(count)

        # Get max of any two adjacent groups added (removing the 0 between them)
        max_pair = max(x+y for x,y in zip(groups, groups[1:]))
        return max_pair
