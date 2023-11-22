class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        cases = []
        return self.rec('', s)

    def rec(self, prefix, s): # Return all upper/lowercase combinations of s with prefix
        if s == '': return [prefix]
        
        if s[0].isalpha(): # If a letter, call recursion with both upper and lowercase version
            return self.rec(prefix+s[0], s[1:]) + self.rec(prefix+s[0].swapcase(), s[1:])
        else:
            return self.rec(prefix+s[0], s[1:])
