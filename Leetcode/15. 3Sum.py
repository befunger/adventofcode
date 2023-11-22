class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        '''
        Given an integer array nums, return all unique triplets of numbers that sum to 0

        Note that we do not care about the indices, only the number combinations. We can sort numbers for more efficient searching.        
        Iterate over each number x. Try to find a pair of numbers that sum to -x to match it.
        '''
        # O(n^2) solution
        output = set()
        n = len(nums)
        nums.sort() # Sort in (hopefully...) O(n log n)

        for i,x in enumerate(nums):
            low = i+1   # Left pointer
            high = n-1  # Right pointer
            while low < high:
                triplet = (x, nums[low], nums[high]) # Note that the values are always in ascending order
                three_sum = sum(triplet)
                if three_sum == 0:
                    if i != low and i != high: # Only add if indices are different and triplet is unique
                        output.add(triplet)
                    low += 1
                    high -= 1
                elif three_sum < 0: # Increase sum by incrementing low pointer
                    low += 1
                else: # Decrease sum by decrementing high pointer
                    high -= 1
        return list(output)


        # Prohibitively slow solution O(n^3) 
        output = []
        dict_of_pairs = {}
        for i,x in enumerate(nums): # Register all pairs O(n^2)
            for j,y in enumerate(nums[i+1:], start=i+1):
                if x+y in dict_of_pairs: # Keep all index pairing, in case there are overlaps in one place but not another
                    dict_of_pairs[x+y].append([i,j])
                else:
                    dict_of_pairs[x+y] = [[i,j]]

        for i,x in enumerate(nums): # Compare all entries to pairs O(n)
            if -x in dict_of_pairs: # Check if a pair matches this entry (if pair has sum -x, triplet has sum 0)
                matching_pairs = dict_of_pairs[-x]
                for pair in matching_pairs:
                    if not i in pair: # Ensure three indexes are unique
                        new_entry = sorted([nums[i], nums[pair[0]], nums[pair[1]]])
                        if not new_entry in output: # Ensure the triplet of values is new
                            output.append(new_entry)
        return output

print(Solution().threeSum([-1,0,1,2,-1,-4]))