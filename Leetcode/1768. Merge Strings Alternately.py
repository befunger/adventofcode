class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ""
        a, b = len(word1), len(word2)
        for i in range(min(a,b)):
            merged += word1[i] + word2[i]
        if a > b:
            merged += word1[b:]
        elif b > a:
            merged += word2[a:]
        return merged
