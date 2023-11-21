class Solution:

    # O(n) solution using cum_sum and strictly increasing walls
    def trap(self, height: List[int]) -> int:
        # We find the highest peak, and iterate towards it from left and right separately O(n)
        n = len(height)
        peak = max(height)
        peak_ind = height.index(peak)
        water = 0

        # cum_sum vector used for calculating number of blocks between two walls O(n)
        cum_sum = [height[0]]*n
        for i in range(1, n):
            cum_sum[i] = cum_sum[i-1] + height[i]

        # Left -> peak O(n)
        i, first_wall = -1, -1
        for j, second_wall in enumerate(height[:peak_ind+1]):
            if i == -1:
                if second_wall > 0: # Add first non-zero to leftWall
                    i, first_wall = j, second_wall
            else:
                if second_wall >= first_wall:
                    water += (j-i-1) * first_wall 
                    water -= cum_sum[j-1] - cum_sum[i]
                    i, first_wall = j, second_wall

        # Right -> peak O(n)
        i, first_wall = -1, -1
        for j, second_wall in enumerate(height[:peak_ind-1:-1] if peak_ind > 0 else height[::-1]):
            if i == -1:
                if second_wall > 0: # Add first non-zero to leftWall
                    i, first_wall = j, second_wall
            else:
                if second_wall >= first_wall:
                    water += (j-i-1) * first_wall
                    water -= cum_sum[-i-2] - cum_sum[-j-1]
                    i, first_wall = j, second_wall

        return water

    # O(nk) where k = max(height)
    def slow_trap(self, height: List[int]) -> int:
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
