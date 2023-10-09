class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        '''
        Find the shortest subarray with a sum >= target, return length of it

        O(n): Sliding window
        O(n^2): Brute force for each starting index

        TODO: O(n log n) binary search for window size? start = 0, end = n
                - Sweep list with window size k = (end - start)/2 in O(n)
                - If none meets target, try again with start = k (larger window size)
                - If target is met, try again with end = k (smaller window size)
                - Return size of smallest that met target
        '''

        # Ensure target is possible
        if sum(nums) < target:
            return 0

        n = len(nums)
        shortestLength = n

        # O(n) sliding window approach.
        # Each step we either move start + 1 or end + 1, at most we move both start and end to the final index, 2n steps.
        # This makes O(n) as long as each step is constant execution
        start = 0
        end = 0
        subSum = nums[0]

        # Start by establishing a first interval. O(n)
        while subSum < target:
            end += 1
            subSum += nums[end]
        shortestLength = end - start + 1
        
        # Scan intervals of 1 smaller size to look for improvement
        subSum -= nums[start]
        start += 1
        
        # Continuously move/shrink sliding window. At most 2n steps before start=end=n. O(n)
        while end < n:
            if subSum >= target:
                shortestLength = end - start + 1
                # Shrink sliding window again
                subSum -= nums[start]
                start += 1
            elif end == n-1: # Kinda stupid fix for going out of index on next step
                return shortestLength
            else:
                # Move sliding window 1 step
                end += 1
                subSum += nums[end] - nums[start]
                start += 1

        return shortestLength

        # O(n^2) solution: For each index find shortest starting at that index (keep adding next index until >= target)
        for i, x in enumerate(nums):
            currentSum = 0
            currentLength = 0
            for j, y in enumerate(nums[i:]):
                currentSum += y
                currentLength += 1
                if currentSum >= target: # If we reach target, record length if new record and then stop
                    shortestLength = min(currentLength, shortestLength)
                    break

        return shortestLength