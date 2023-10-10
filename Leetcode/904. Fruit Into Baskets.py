class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        ''' Get length of the longest subarray containing at most 2 unique numbers

        O(n) implementation: Keep track of subarray thus far with at most 2 unique, and at most 1 unique

        In terms of fruit:
        One bag holds ORANGES and PEARS, and the other PEARS.
        Once we reach an APPLE, retire the ORANGES and PEARS bag. Turn PEARS bag into PEARS and APPLES, and start new bag with APPLES.
        '''

        current = [None, None]  # Bookkeeps current 2 fruit types
        amounts = [0]           # Stack storing values of bags we fill

        print(fruits)
        for i, _ in enumerate(fruits):
            if not fruits[i] in current: # New fruit, push new bag onto stack
                current = [current[1], fruits[i]]
                amounts.append(0)
            elif fruits[i] == current[0]: # Previous fruit returning, reset single-fruit bag (its amount is superceded by the double bag anyways)
                current = [current[1], fruits[i]]
                amounts[-1]  = 0
            amounts[-1] += 1
            amounts[-2] += 1

        return max(amounts)
