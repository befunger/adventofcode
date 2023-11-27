class Solution:
    def compress(self, chars: List[str]) -> int:
        p = 0  # Pointer to index for writing in array
        count, curr = 0, chars[0]
        for char in chars:
            if char == curr:
                count += 1
            else: # Write 
                p = self.write(chars, curr, count, p)
                curr, count = char, 1

        p = self.write(chars, curr, count, p)
        return p

    def write(self, array, char, count, p):
        # Writes char and count to the array and returns updated pointer p
        array[p] = char
        p += 1
        if count > 1:
            for digit in str(count): 
                array[p] = digit
                p += 1
        return p
