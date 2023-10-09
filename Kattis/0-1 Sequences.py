inp = input()

onesOnLeft = 0   # Number of 1s on left
blanks = 0       # Number of ?'s encountered
tot = 0          # Total inversions needed (scaled down by 2^k)

for i in inp:
    if i == "0":
       tot = (tot + onesOnLeft) % (1000000007)
    elif i == "1":
        onesOnLeft = (onesOnLeft + 1)
    elif i == "?":
        tot = (tot + 0.5*onesOnLeft) % 1000000007
        onesOnLeft = (onesOnLeft + 0.5)
        blanks = (blanks + 1)


for _ in range(blanks):
    tot = (2*tot) % 1000000007
print(int(tot))