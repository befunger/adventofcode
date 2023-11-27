class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Area is given by min(height[i], height[j])*(j-i)
        # Find i and j that maximise area
        i = 0
        j = len(height)-1
        max_water = 0 # Rectangle spanned by shortest of heights and horizontal distance
        while(i < j):
            # Update max water if current is higher
            max_water = max(max_water, min(height[i],height[j])*(j-i))
            # Move the pillar with lower height inward in search of higher
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max_water
        
        # Bruteforce in O(n^2)
        max_water = 0
        for i,x in enumerate(height):
            for j,y in enumerate(height[i+1:], start=i+1):
                max_water = max(max_water, min(x,y)*(j-i))
        return max_water