class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        '''
        PROBLEM: Return start indices of all anagrams of s in p

        SOLUTION: This is very similar to Problem 567 (Find if permutation of s in p) 
        Instead of returning true, we return the starting index of each window that fulfills the original problem criteria. 

        '''
        indices = []

        size = len(p)
        s1_counts = [0]*26
        window_counts = [0]*26

        for char in p:
            s1_counts[ord(char)-ord('a')] += 1

        for ind,char in enumerate(s):
            window_counts[ord(char)-ord('a')] += 1
            if ind >= size:
                window_counts[ord(s[ind-size])-ord('a')] -= 1 # Remove entries outside of window size
            if window_counts == s1_counts:
                indices.append(ind-size+1) # Starting index of window that matches
        return indices

print(Solution().findAnagrams(
    s = "cbaebabacd", p = "abc"
))
