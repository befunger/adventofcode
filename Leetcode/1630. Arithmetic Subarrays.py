class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        # In an arithmetic sequence all elements are strictly increasing/decreasing
        # Sorting the list and checking that all differences between adjacent are same is enough
        # m queries, each sorting O(n log n) and stepping through O(n) nums => O(m * n log n)
        # Perhaps can improve to O(m * n)? 
        return [self.canMakeArithmetic(nums[a:b+1]) for (a,b) in zip(l, r)]

    def canMakeArithmetic(self, arr):
        # Returns true/false depending on if nums can be arranged to an arithmetic.
        n = len(arr)
        if n <= 2: return n == 2 # Returns true for length 2, false for length 0 and 1
        arr = sorted(arr)
        step = arr[1] - arr[0]
        for i in range(n-1):
            if arr[i+1] - arr[i] != step: return False
        return True
