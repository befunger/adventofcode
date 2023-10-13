class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        '''
        Square elements (including negative numbers) and return sorted result. 

        O(n) approach:
        Find split between negative/positive numbers in O(n)
        Square all numbers O(n)
        Do a merge sort of the two subarrays in O(n)
        '''
        n = len(nums)
        positive_index = n

        for i,x in enumerate(nums): # Square elements and find midpoint between positive and negative O(n)
            if x >= 0 and positive_index == n:
                positive_index = i
            nums[i] *= nums[i]

        negative_index = positive_index - 1

        sorted_squares = [0]*n
        index = 0
        while index < n:
            # Pick whichever number is greater from positive and negative pointer (or default to other if either out of range)
            if positive_index < n and (negative_index < 0 or nums[positive_index] < nums[negative_index]):
                sorted_squares[index] = nums[positive_index]
                positive_index += 1
            else:
                sorted_squares[index] = nums[negative_index]
                negative_index -= 1
            index += 1 # Loop is O(n) as it executes at most n times

        return sorted_squares

        '''Quick and simple O(n log n)'''
        for i,_ in nums:
            nums[i] *= nums[i]
        nums.sort()
        return nums

print(Solution().sortedSquares(nums = [-4,-1,0,3,10]))