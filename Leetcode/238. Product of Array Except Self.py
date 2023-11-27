class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [a, b, c, d] => [b*c*d, a*c*d, a*b*d, a*b*c]
        # Calculate all prefixes in O(n) time
        # Calculate all suffixes in O(n) time
        # output[i] = prefix until i * suffix after i 
        # Make O(1) space by storing suffixes in output -> prefixes in input -> overwrite result in output
        n = len(nums)

        # Calculate suffix products
        output = [1]*n
        for i in range(n-1, 0, -1): # From n-1 -> 1
            output[i-1] = output[i]*nums[i]

        # Calculate prefix products
        for i in range(n-1): # From 0 -> n-2
            nums[i+1] = nums[i+1]*nums[i]
        nums[-1] = 1 # Ensures ouput[1] calculated correctly

        # Calculate result products
        for i in range(n):
            output[i] = nums[i-1]*output[i]
        return output
