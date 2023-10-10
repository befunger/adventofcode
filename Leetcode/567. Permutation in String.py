class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''
        PROBLEM: Return true/false depending on if a permutation of s1 exists in s2
        
        Sliding window of s1.size, check if all characters of s1 in window.
        Rechecking at each index can make O(n^2) since s1 can be just as long as s2.
        At each window movement, remove first element and add new last.
        
        How to check if permutation quickly? 
        Use 26-arrays of counts, compare in O(1).
        '''
        size = len(s1)
        s1_counts = [0]*26
        window_counts = [0]*26

        for char in s1:
            s1_counts[ord(char)-ord('a')] += 1

        for ind,char in enumerate(s2):
            window_counts[ord(char)-ord('a')] += 1
            if ind >= size:
                window_counts[ord(s2[ind-size])-ord('a')] -= 1 # Remove entries outside of window size
            if window_counts == s1_counts:
                return True
        return False

print(Solution().checkInclusion(
    s1 = "gas"  , s2 = "dcdaasgeasd"
))