class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # In each step, we can either add an open or closed bracket or both.
        # - Can only add closed if an open one exists
        # - Can only add open if still open ones left
        return self.rec(n, 0, 0, '')

    def rec(self, n, opened, closed, prefix):
        if opened == n and closed == n: return [prefix]
        output = []
        if opened < n: 
            output.extend(self.rec(n, opened+1, closed, prefix+"("))
        if closed < opened: 
            output.extend(self.rec(n, opened, closed+1, prefix+")"))
        return output
