class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        '''
        Return indices of two numbers in nums that sum to target
        
        O(n^2): Just iterate twice and check sum

        Faster?
        Sort list in O(n log n)
        For each number, use binary search to find if matching to target exists in O(log n)
        Find indices of correct numbers in O(n)
        '''

        # Fastest O(n) solution:
        num_index_dict = {}
        for i,x in enumerate(nums):
            if target-x in num_index_dict:
                return [i, num_index_dict[target-x]]
            else:
                num_index_dict[x] = i

        # Binary search solution O(n log n):
        sorted_nums = sorted(nums)
        for i,x in enumerate(nums):
            if self.binary_search(sorted_nums, target-x):
                j = nums.index(target-x)
                if i != j:
                    return [i, j]

        # Slower python solution O(n log n)
        for i,x in enumerate(nums):
            if target-x in nums:
                j = nums.index(target-x)
                if i != j:
                    return [i, j]

        # Even slower O(n^2) double-iterate solution
        for i,x in enumerate(nums):
            for j,y in enumerate(nums):
                if x+y == target and i != j:
                    return [i, j]

    def binary_search(self, arr, target):
        '''Returns True or False depending on if target exists in array'''
        left = 0
        right = len(arr) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] == target:
                return True  # Element found
            elif arr[mid] < target:
                left = mid + 1  # Search in the right half
            else:
                right = mid - 1  # Search in the left half
        return False  # Element not found
