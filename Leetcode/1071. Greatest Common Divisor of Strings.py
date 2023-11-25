from math import gcd
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # The gcd is the largest substring k such that A = k * n, B = k * m, for integers n,m
        # If there is a common divisor (assume n >= m) then B is equal to the first k*m characters in A:
        # => B = A[:k*m] (or vice versa if m > n)
        if str1 + str2 != str2 + str1: return ""

        string_gcd = gcd(len(str1), len(str2))
        return str1[:string_gcd]
        
        
