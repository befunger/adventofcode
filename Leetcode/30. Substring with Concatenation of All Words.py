from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        '''
        Find any substring of s that contains all the strings in words in some arbitrary order.
        (Individual words must be intact, but any permutation of the ordering is ok)

        Scan across the string one word_length at a time, use Counter to keep track of which words are missing
        Note down index when all counter entries are at 0
        We need to repeat the full scan-through to ensure we find matching substrings that are offset from the start of the string
        '''
        indices = []
        word_size = len(words[0])
        window_size = word_size*len(words)
        string_size = len(s)

        for offset in range(word_size): # Go through the whole string with offsets to find any permutations not aligned to start
            counter_list = Counter(words)
            for i in range(0,string_size//word_size): # Iterate through every word-sized chunk
                start = i*word_size+offset
                word = s[start:start+word_size] # Add word at end of window
                counter_list[word] -= 1
                if i*word_size >= window_size: # Remove word from start of window
                    old_word = s[start-window_size:start-window_size+word_size]

                    counter_list[old_word] += 1
                if not any(counter_list.elements()): # When all counters are at 0, we have a match
                    indices.append(start-window_size+word_size) # First index of words in counter_list
        return indices

print(Solution().findSubstring(s = "barfoothefoobarman", words = ["foo","bar"]))
print(Solution().findSubstring(s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]))
print(Solution().findSubstring(s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]))
print(Solution().findSubstring(s = "lingmindraboofooowingdingbarrwingmonkeypoundcake", words = ["fooo","barr","wing","ding","wing"]))
print(Solution().findSubstring(s = "wordgoodgoodgoodbestword", words = ["word","good","best","good"]))
