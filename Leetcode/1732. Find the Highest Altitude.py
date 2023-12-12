class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        current = highest = 0
        for x in gain:
            current += x
            highest = max(current, highest)
        return highest
