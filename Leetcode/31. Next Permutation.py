class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Find largest i where nums[i] < nums[i-1], swap and sort all nums[i-1:end] 
        n = len(nums)
        if n == 1: return

        # Find rightmost index with non-increasing next number
        i = n-2
        while(i >= 0 and nums[i] >= nums[i+1]):
            i -= 1
        
        # If i == -1, whole list is in descending order, so reverse everything 
        if i == -1:
            nums[:] = nums[::-1]
        else:
            # Find smallest in nums[i:] that is larger than nums[i]
            j = n-1 
            while(nums[i] >= nums[j]): j -= 1
            # Swap
            nums[i], nums[j] = nums[j], nums[i]

            # Sort nums[i:] in reverse
            nums[i+1:] = nums[n-1:i:-1]
