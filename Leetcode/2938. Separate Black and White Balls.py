class Solution:
    def minimumSteps(self, s: str) -> int:
        # To sort the array, each 0 (white ball) must be swapped with each black ball (1) on its left
        ones_passed, swaps = 0, 0
        for bit in s:
            if bit == "1":
                ones_passed += 1
            else:
                swaps += ones_passed
        return swaps
