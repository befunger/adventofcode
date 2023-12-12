class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # Collect first k
        average = max_average = sum(nums[:k])

        # Slide window and update max average
        for i in range(k, len(nums)):
            average += nums[i] - nums[i-k]
            max_average = max(average, max_average)

        # Return average
        return max_average/k
