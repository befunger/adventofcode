class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        # A pair is nice if their self-difference is the same
        pairs = 0
        diff_counts = {}
        mod = 10**9 + 7

        for num in nums:
            # Calculate self-diff
            diff = num - self.revNum(num)
            # Match all previous with same self-diff
            if diff in diff_counts:
                pairs = (pairs + diff_counts[diff]) % mod 
                diff_counts[diff] += 1
            else: # Else, make new entry
                diff_counts[diff] = 1
        return pairs

    def revNum(self, num: int):
        # Reverse the number and return it (removes leading 0s with int())
        return int((str(num)[::-1]))