class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        Longest substring of same character with k infractions

        Keep k bags? (One for each "amount" of fixed characters). Likely O(n^2) since k = O(n)
        Abuse fact that only 26 = O(1) letters in english alphabet? (For each letter find longest)
        '''
        longest = 0

        for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            start = 0
            reps = k
            current_length = 0
            for x in s:
                # Loop invariant: After loop is finished current_length holds the length of best solution ending at x
                if x != letter:
                    if reps > 0: # Use one of remaining replacements
                        reps -= 1
                    else: # Move start until we pass a replacement
                        while s[start] == letter:
                            start += 1
                            current_length -= 1
                        start += 1
                        current_length -= 1

                current_length += 1
                longest = max(longest, current_length)

        return longest
