FNAME = "in3.txt"
    
def parse_line(line):
    return [int(i) for i in line]

data = [parse_line(line) for line in open(FNAME).read().splitlines()]

# take in an array of integer values and find the max joltage
# basically find the max digit in all but the last spot
# then combine with the max remaining digit after the first 
# instance of the true max
def max_jolt(line):
    first_digit = max(line[:-1])
    i = line.index(first_digit)
    second_digit = max(line[i + 1:])
    return 10 * first_digit + second_digit

part1 = sum(max_jolt(line) for line in data)
print("Part 1:", part1) # 17085

# now we also take parameter i which is the number of digits we want
# which allows this problem to be solved recursively
# same basic idea: find the max digit in all but last (i - 1) digits
# then find the max remaining digit in all but the last (i - 2) digits...
def max_jolt(line, i):
    if i == 1:
        return max(line)
    first_digit = max(line[:-(i - 1)])
    j = line.index(first_digit)
    rest = max_jolt(line[j + 1:], i - 1)
    return first_digit * 10 ** (i - 1) + rest #int(str(first_digit) + str(rest))
    
part2 = sum(max_jolt(line, 12) for line in data)
print("Part 2:", part2) # 169408143086082
