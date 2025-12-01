FNAME = "in1.txt"

# convert each input value into a signed number    
def parse_line(line):
    direction, value = line[0], int(line[1:])
    if direction == 'L':
        return -value
    else:
        return value

data = [parse_line(line) for line in open(FNAME).read().splitlines()]

part1 = 0
part2 = 0
pos = 50

for d in data:
    
    before = pos
    pos += d
    
    # there is probably a cleaner way...
    if pos == 0:
        part2 += 1
    elif before > 0 and pos < 0:
        part2 += abs(pos) // 100 + 1
    elif before == 0 and pos <= -100:
        part2 += abs(pos) // 100
    elif pos >= 100:
        part2 += pos // 100
 
    pos %= 100
    if pos == 0:
        part1 += 1
    
print("Part 1:", part1) # 997
print("Part 2:", part2) # 5978
