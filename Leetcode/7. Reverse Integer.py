class Solution:
    def reverse(self, x: int) -> int:
        # Circumvent comparing potential 64-bit integers by performing a lexigraphical comparison with a string
        if x < 0:
            num = str(x)[-1:0:-1]
            num = "0"*(10-len(num)) + num
            if num > "2147483648": return 0
            return -int(num)
        else: 
            num = (str(x)[::-1])
            num = "0"*(10-len(num)) + num
            if num > "2147483647": return 0
            return int(num)
