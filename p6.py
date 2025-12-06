from aoc_utils import *
from math import prod

FNAME = "in6.txt"

# parse the input file 
# into a sequence of value (operand) vectors 
# and a sequence of operators
data = [line.split() for line in open(FNAME).read().splitlines()]
values = [[int(i) for i in line] for line in data[:-1]]
operands = data[-1]
value_vectors = transpose(values)

part1 = 0

# loop through each problem, evaluating it
for value_vector, operand in zip(value_vectors, operands):
    if operand == '+':
        part1 += sum(value_vector)
    else:
        part1 += prod(value_vector)
        
print("Part 1:", part1) # 6635273135233

# now parse the file as a large array of individual characters
data = [list(line) for line in open(FNAME).read().splitlines()]
data = transpose(data)

# each problem will look something like this now:
# data[:4] ->
# ['7', '2', '2', '6', '*']
# ['2', '5', '6', '8', ' ']
# ['4', '7', '8', '5', ' ']
# [' ', ' ', ' ', ' ', ' ']
# so we need to read a stream starting with
# a line containing a value and then an operand
# then one or more (?) other values
# and finally a blank line
# so we need to loop through the rows in a stream processing fashion
part2 = 0
new_calc = True # are we ready to start a new problem?

# simplified processing if *every* problem has a blank line after it, 
# even the last one
data.append([' ']) 

for row in data:
    
    # if we're starting a new problem, we need a fresh slate
    if new_calc:
        value_vector = [int(''.join(row[:-1]))] # grab the value
        operand = row[-1] # grab the operand
        new_calc = False # we are now "in flight"
        
    # if we've reached a blank line,
    # it's time to execute the calculation and prepare for next round
    elif all(i == ' ' for i in row):
        if operand == '+':
            part2 += sum(value_vector)
        else:
            part2 += prod(value_vector)
        new_calc = True
        
    # otherwise, we're at an intermediate value,
    # which we just need to capture
    else:
        value_vector.append(int(''.join(row)))   

print("Part 2:", part2) # 12542543681221
