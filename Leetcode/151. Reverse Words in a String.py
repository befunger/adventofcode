class Solution:
    def reverseWords(self, s: str) -> str:
        # Iterate from back with two points. Move j until non-space char and i until first preceeding non-space char
        # Add s[i,j] to output and set j to i-1
        i, j = 0, 0
        end = len(s) - 1
        words = []

        # Retrieve words without extra spaces
        while i <= end:
            if s[i] != ' ': # Found start
                j = i+1
                while j <= end and s[j] != ' ':
                    j += 1
                words.append(s[i:j] if j <= end else s[i:])
                i = j
            i += 1

        # Reverse and stitch together with spacebars
        output = ""
        for i,x in enumerate(words[::-1]):
            if i != 0:
                output += " "
            output += x

        return output

        # Pythonic 1-line
        return ' '.join([word for word in s.split(' ')[::-1] if word])
