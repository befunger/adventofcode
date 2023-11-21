class Solution:
    # O(nk) where k = max(height)
    def trap(self, height: List[int]) -> int:
        water = 0
        for level in range(max(height)):
            i = -1
            for j, val in enumerate(height):
                if val > level and i == -1:
                    i = j
                elif val > level and i >= 0:
                    water += (j - i - 1) # Amount of blocks between walls at i and j
                    i = j
        return water
