class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        longest = 0
        start = 0
        current_length = 0
        for x in nums:
            # Loop invariant: After loop is finished current_length holds the length of best solution ending at x
            if x != 1:
                if k > 0: # Use one of remaining replacements
                    k -= 1
                else: # Move start until we pass a replacement
                    while nums[start] == 1:
                        start += 1
                        current_length -= 1
                    start += 1
                    current_length -= 1

            current_length += 1
            longest = max(longest, current_length)

        return longest

print(Solution().longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2)) # 6
