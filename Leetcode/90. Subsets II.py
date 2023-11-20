class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # Same as subset, but the n:th duplicate is added only to sets with n-1 of the number
        # Otherwise, we will spawn duplicate sets.
        ''' 
        For example, if nums = [1, 2, 2]
            Start:  ans = [[]]
            Add 1:  ans = [[], [1]]
            Add 2:  ans = [[], [1], [2], [1, 2]]
            Add 2:  ans = [[], [1], [2], [1, 2], [2, 2], [1, 2, 2]] (Only add to [2] and [1,2])
            Add 2:  Add only to [2, 2] and [1, 2, 2]
        '''
        ans = [[]]
        uniques = {}
        for num in nums:
            ans += [s + [num] for s in ans 
                    if not num in uniques               # Add new number to all sets
                    or s.count(num) == uniques[num]]    # Add n:th dupe only to sets which already have n-1 of that number
            uniques[num] = 1 if not num in uniques else uniques[num]+1 # uniques[num] holds count of num encountered
        return ans
