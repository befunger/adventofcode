import regex as re
with open("AoC 2023\inputs\day1.txt", "r") as file:
    inp = file.readlines()

# Part 1
digits = [re.findall("\d", line) for line in inp] # Retrieve all digits (0-9)
nums = [int(a[0]+a[-1]) for a in digits] # Append first and last
print(sum(nums))

# Part 2
def parse_digit(s):
    '''Convert written out digits to numerical'''
    if len(s) == 1: return s
    stoi = {"one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}
    return stoi[s]

digits = [re.findall("\d|one|two|three|four|five|six|seven|eight|nine", line, overlapped=True) for line in inp]
nums = [int(parse_digit(a[0])+parse_digit(a[-1])) for a in digits]
print(sum(nums))
