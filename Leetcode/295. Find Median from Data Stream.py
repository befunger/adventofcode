from heapq import *
class MedianFinder:

    def __init__(self):
        self.upperHeap = [] # Holds upper 'half' of numbers with minimum at top
        self.lowerHeap = [] # Holds lower 'half' of numbers with maximum at top (we use negatives to turn min into max heap)

    def addNum(self, num: int) -> None:
        # Same number of entries --> Add to upper
        if len(self.lowerHeap) == len(self.upperHeap):
            if(len(self.lowerHeap) == 0 or num >= -self.lowerHeap[0]): # Add directly to upper
                heappush(self.upperHeap, num)
            else: # Shift top from lower, and add num
                heappush(self.upperHeap, -heappop(self.lowerHeap))
                heappush(self.lowerHeap, -num)
        # Not same --> One more on upper --> Add to lower
        else:
            if(num > self.upperHeap[0]): # Shift bottom from upper, and add num
                heappush(self.lowerHeap, -heappop(self.upperHeap))
                heappush(self.upperHeap, num)
            else: # Add directly to lower
                heappush(self.lowerHeap, -num)
            

    def findMedian(self) -> float:
        if len(self.upperHeap) == len(self.lowerHeap):
            return (self.upperHeap[0] - self.lowerHeap[0])/2
        else:
            return self.upperHeap[0]
