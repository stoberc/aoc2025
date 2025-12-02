FNAME = "in2.txt"
    
def parse_line(line):
    a, b = line.split('-')
    return int(a), int(b)

data = [parse_line(line) for line in open(FNAME).read().split(',')]

# split a string into the first half and the second half
def halves(i):
    assert type(i) == type("adsf")
    assert len(i) % 2 == 0
    return i[:len(i)//2], i[len(i)//2:]
    
# checks if an int id is valid
def is_valid(i):
    i = str(i)
    if len(i) % 2 == 1:
        return True
    j, k = halves(i)
    if j == k:
        return False
    return True

# find the total of all invalid ids on the interval [a, b]
# I thought this would require something more clever than brute forcing through
# the entire range, but this worked    
def invalid_id_total(a, b):
    total = 0
    for i in range(a, b + 1):
        if not is_valid(i):
            total += i
    return total
        
part1 = sum(invalid_id_total(a, b) for a, b in data)
print("Part 1:", part1) # 30608905813

# take a string, i, and split it into chunks of size j
# example: get_pieces("abcdefghijk", 3) returns ["abc", "def", "ghi", "jk"]
# perfect divisibility is not really a problem here
def get_pieces(i, j):
    return [i[k:k+j] for k in range(0, len(i), j)]
    
# redefine what validity means for part 2
def is_valid(i):
    i = str(i)
    for j in range(1, len(i) // 2 + 1):
        pieces = get_pieces(i, j)
        if len(set(pieces)) == 1:
            return False
    return True
    
part2 = sum(invalid_id_total(a, b) for a, b in data)
print("Part 2:", part2) # 31898925685
