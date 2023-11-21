class Solution:
    def minimumSteps(self, s: str) -> int:
        ones_passed, swaps = 0, 0
        for bit in s:
            if bit == "1": 
                ones_passed += 1
            else:
                swaps += ones_passed
        return swaps