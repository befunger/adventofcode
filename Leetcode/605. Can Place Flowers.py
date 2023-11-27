class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0: return True
        planted = 0
        plots = len(flowerbed)
        for i,_ in enumerate(flowerbed): # No flower on left, no flower on right, no flower on plot
            if(i == 0 or flowerbed[i-1] == 0) and (i == plots-1 or flowerbed[i+1] == 0) and flowerbed[i] == 0:
                planted += 1
                flowerbed[i] = 1
                if planted >= n: return True
        return False
