class Solution:
    def minWindow(self, s: str, t: str) -> str:
        '''
        Given two strings s and t, return the smallest substring of s that includes every character in t (duplicates included)

        Similar to Problem 567 (Ascertain if a permutation of t exists in s), but we wish to find
        the 'closest' solution rather than only a *perfect* permutation.

        Approach:
        We use count lists to keep track of letter frequencies t_count and window_count
        The sum of differences window_count - t_count gives the "distance"
        Distance 0 indicates perfect anagram, and positive if window is larger.
        Note that ALL differences MUST be 0 or positive, or else we are missing characters from t.

        Start by increasing window size until we match.
        Once match is found, decrease size by 1 and translate until better match (no point looking for equal/worse matches)
        '''
        if len(s) < len(t): # Substring can't be greater
            return ""

        # Set up count arrays
        t_counts = [0]*52
        window_counts = [0]*52
        for char in t:
            t_counts[self.ind(char)] += 1

        count_dist = -1
        best_string = ""
        start = 0
        end = 0
        while end < len(s) or count_dist >= 0:
            if count_dist >= 0:
                best_string = s[start:end]
            else:
                window_counts[self.ind(s[end])] += 1 # Expand window, except if finding new best (in order to shrink window)
                end += 1

            if best_string != "": # Once finding a single solution, we slide window
                window_counts[self.ind(s[start])] -= 1
                start += 1

            count_dist = self.count_distance(window_counts, t_counts)

        return best_string

    def count_distance(self, count: list[int], goal_count: list[int]) -> int:
        '''Helper function for count distances'''
        diffs = [count[i] - goal_count[i] for i in range(52)]
        if min(diffs) < 0:
            # A goal failed to be met
            return -1
        else:
            return sum(diffs)

    def ind(self, letter):
        '''Helper function for indexing letters'''
        order = ord(letter)
        if order >= 97:
            return order - ord('a')
        return order - ord('A') + 26
