class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # Two strings are close if they can be made equal using the following operations:
        # (a): Swap places of two characters
        # (b): Invert the occurences of two characters (all x become y, all y become x)

        # Two strings can never be equal if
        # - They have different length
        # - One contains a type of character not present in the other

        # Under (a), all permutations are equal
        # Under (b), we can swap the number of characters of two present types within the word
        # (b) means, that as long as all the right letters are present
        # and the list of quantities of letters are the same between both words
        # we can swap the quantities around (using operation 2) and then move letters around
        # (using operation 1) and match the words

        # Get sets of unique characters in the two words (these must be the same)
        set1 = set(word1)
        set2 = set(word2)

        # Get sorted lists of quantities in each word
        counts1 = sorted([word1.count(x) for x in set1])
        counts2 = sorted([word2.count(x) for x in set2])

        return set1 == set2 and counts1 == counts2
