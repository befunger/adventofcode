class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        Longest substring of same character with k infractions

        Keep k bags? (One for each "amount" of fixed characters). Likely O(n^2) since k = O(n)
        Abuse fact that only 26 = O(1) letters in english alphabet? (For each letter find longest)
        Onepass, but keep track of which is the character that appears most often in the solution (becomes O(n^2)?
        '''

        '''Fast bruteforce solution iterating alphabet'''
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

        '''Onepass solution with updating letter variable, quite slow due to possible O(n^2) complexity from finding most frequent letter'''
        longest = 0
        sub_string = ''
        for x in s:
            # Loop invariant: After loop is finished longest holds the length of best solution ending at x or earlier
            sub_string += x # Expand window
            freq = [(c, sub_string.count(c)) for c in set(sub_string)]
            letter, letter_count = max(freq, key=lambda x: x[1]) # Gets most frequent character in substring
            
            print(f"{letter} is the most frequent in {sub_string} with count {letter_count}")
            if len(sub_string) - letter_count > k: # Too many errors, slide window
                sub_string = sub_string[1:]
                print(f"{len(sub_string) - letter_count} errors. Updating to {sub_string}")
            else: # Acceptable errors, update longest if applicable
                print(f"Managable errors. Keeping expanded window of length {len(sub_string)}")
                longest = max(longest, len(sub_string))

        return longest



s = Solution()
print(s.characterReplacement("AABABBA", 1))
