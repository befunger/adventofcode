class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        '''
        Given an integer array nums, return the sum of 3 values closest to target

        The problem is very similar to 3Sum, except we find the closest sum instead of all triplets that sum to target 0
        '''
        # O(n^2) solution
        n = len(nums)
        nums.sort()
        closest = 999999999

        for i,x in enumerate(nums):
            low = i+1   # Left pointer
            high = n-1  # Right pointer
            while low < high:
                three_sum = x + nums[low] + nums[high]
                if i != low and i != high and abs(target - three_sum) < abs(target - closest): # Only add if indices are different and triplet is unique
                    closest = three_sum
                elif three_sum < target: # Increase sum by incrementing low pointer
                    low += 1
                else: # Decrease sum by decrementing high pointer
                    high -= 1
        return closest
