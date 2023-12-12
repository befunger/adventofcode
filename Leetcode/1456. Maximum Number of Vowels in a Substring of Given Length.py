class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}

        # Collect first k chars
        num_vowels = 0
        for i in range(k):
            # Parse bool to int 0 or 1
            num_vowels += int(s[i] in vowels)

        max_vowels = num_vowels
        
        # Slide window and update max
        for i in range(k, len(s)):
            num_vowels += int(s[i] in vowels) - int(s[i-k] in vowels)
            max_vowels = max(num_vowels, max_vowels)
        
        return max_vowels
