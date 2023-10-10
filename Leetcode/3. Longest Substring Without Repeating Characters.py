class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        Sliding window approach
        O(n) due to fast set operations
        Outer loop runs n times. While loop runs at most n times across *whole execution* (start increments by one every time)
        '''

        in_window = set() # Set for storing current values in window (Avoids O(n) comparing)
        max_length = 0
        start = 0

        for _, x in enumerate(s):
            while x in in_window: # Remove from the start of window until next char available again
                in_window.remove(s[start])
                start += 1
            in_window.add(x)
            max_length = max(max_length, len(in_window)) # Maintain max

        return max_length
