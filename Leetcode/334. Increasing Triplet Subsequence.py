class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # Our goal is that j_val always has the lowest encountered value with a smaller value to the left
        # This way, as soon as we find a value higher than j we can return true
        min_val = i_val = j_val = float('inf')

        for ind, val in enumerate(nums):
            # Keep track of lowest historically (Useful for when we find a value lower than i at index higher than j)
            if val < min_val: min_val = val

            # k found
            if val > j_val: return True

            # Smaller j that adheres to val_i < val_j
            elif val < j_val and val > i_val:
                j_val = val

            # Smaller j that adheres if we replace val_i with min_val
            elif val < j_val and val > min_val:
                i_val = min_val
                j_val = val

        return False
